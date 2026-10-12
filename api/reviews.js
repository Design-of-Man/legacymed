// GET /api/reviews — live Google rating and recent reviews for the practice.
//
// Needs GOOGLE_PLACES_API_KEY (Places API (New) enabled) and, ideally,
// GOOGLE_PLACE_ID. Without a place ID it looks the practice up once by text
// search. Responses are cached at the edge for 12 hours. Without a key it
// answers 503, and the site never calls it: build.py only wires the live
// reviews block into the HTML when the key exists at build time.
"use strict";

const QUERY = "Legacy Medical Concierge Dr. Yana Shtern, 11380 Prosperity Farms Rd Suite 114, Palm Beach Gardens, FL 33410";

module.exports = async (req, res) => {
  const key = process.env.GOOGLE_PLACES_API_KEY;
  if (!key) {
    res.setHeader("Cache-Control", "no-store");
    return res.status(503).json({ ok: false, error: "not_configured" });
  }
  const headers = { "X-Goog-Api-Key": key, "Content-Type": "application/json" };
  try {
    let id = process.env.GOOGLE_PLACE_ID;
    if (!id) {
      const s = await fetch("https://places.googleapis.com/v1/places:searchText", {
        method: "POST",
        headers: Object.assign({ "X-Goog-FieldMask": "places.id" }, headers),
        body: JSON.stringify({ textQuery: QUERY, maxResultCount: 1 }),
      });
      const sj = await s.json();
      id = sj && sj.places && sj.places[0] && sj.places[0].id;
      if (!id) throw new Error("place not found");
    }
    const r = await fetch("https://places.googleapis.com/v1/places/" + encodeURIComponent(id), {
      headers: Object.assign({ "X-Goog-FieldMask": "rating,userRatingCount,reviews,googleMapsUri" }, headers),
    });
    if (!r.ok) throw new Error("places status " + r.status);
    const p = await r.json();
    const out = {
      ok: true,
      rating: p.rating || null,
      count: p.userRatingCount || 0,
      url: p.googleMapsUri || null,
      reviews: (p.reviews || []).map((v) => ({
        author: (v.authorAttribution && v.authorAttribution.displayName) || "Google user",
        rating: v.rating || null,
        text: (v.text && v.text.text) || (v.originalText && v.originalText.text) || "",
        when: v.relativePublishTimeDescription || "",
      })),
    };
    res.setHeader("Cache-Control", "public, s-maxage=43200, stale-while-revalidate=86400");
    return res.status(200).json(out);
  } catch (e) {
    console.error("reviews:", e.message);
    res.setHeader("Cache-Control", "public, s-maxage=300");
    return res.status(502).json({ ok: false, error: "upstream" });
  }
};
