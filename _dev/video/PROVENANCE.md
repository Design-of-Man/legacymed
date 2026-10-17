# Hero video

> **Current encode (Oct 17, 2026): the Juno Beach Pier clip.** Requested by Design of Man: the same drone shot as the
> RegenOrtho hero. Everything below the first rule describes earlier encodes and is kept for history.
>
> - Source: Dropbox `/Nicholas Kashuba/kashuba/Juno.MP4`, 2688x1512 H.264, 59.94 fps, 938 frames (15.65 s), 175,925,573 bytes,
>   sha256 `e17a2c754a4e680a5cf2a33e915503fa71d1471b642d005843410db726360443`. This is the camera's native resolution:
>   there is no 4K master, so nothing here is upscaled past 1512.
> - The drone's auto-exposure dips crossing the pier (mean luma 127 down to 110 at ~8.5 s) and snaps up to 134 at 9.0 s.
>   The loop uses RegenOrtho's edit to hide that inside a dissolve: A = 1.0-8.2 s (pier approach), B = 9.6-15.65 s
>   (post-pier glide), C = 0.55-1.15 s (wrap stub), all slowed to 0.8x and set to 30 fps, A->B crossfade 1.2 s at 7.8 s,
>   ->C crossfade 0.6 s at 14.7625 s. Result: 466 frames, 15.53 s.
> - **Grade: a little darker.** The owner asked (Oct 17) for the film "a bit darker as to flow into our color scheme".
>   The loop master goes through `curves=all='0/0 0.25/0.19 0.5/0.40 0.75/0.64 1/0.90'` into `graded.mp4`
>   (mean luma about 15% lower: 123 to 104 on a mid-approach frame; highlights capped at 90% so the sand stops glaring).
>   Three strengths were compared side by side; this was the middle one, the strongest that still reads as natural.
>   It is baked into the files, not a CSS overlay. RegenOrtho's brightening grade (`eq=gamma=1.12:...`) is not used.
> - Sets: `hd` = 1080p, `qhd` and `uhd` = native 1512p (H.264 fallback for both is the 1080p file). Portrait phones get
>   the 850x1512 crop at x=919 (the same crop RegenOrtho uses; the pier stays in frame throughout).
>
> ```sh
> SRC=Juno.MP4
> C="-color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv"
> ffmpeg -i $SRC -filter_complex "[0:v]split=3[a][b][c];\
> [a]trim=1.0:8.2,setpts=(PTS-STARTPTS)/0.8,fps=30[A];\
> [b]trim=9.6:15.65,setpts=(PTS-STARTPTS)/0.8,fps=30[B];\
> [c]trim=0.55:1.15,setpts=(PTS-STARTPTS)/0.8,fps=30[Cc];\
> [A][B]xfade=transition=fade:duration=1.2:offset=7.8[AB];\
> [AB][Cc]xfade=transition=fade:duration=0.6:offset=14.7625,format=yuv420p[v]" \
>  -map "[v]" -an -c:v libx264 -preset medium -crf 6 $C master.mp4
> ffmpeg -i master.mp4 -vf "curves=all='0/0 0.25/0.19 0.5/0.40 0.75/0.64 1/0.90',format=yuv420p" -an -c:v libx264 -preset medium -crf 6 $C graded.mp4
> # every rendition and the poster below read graded.mp4 (written as master.mp4 for brevity)
> A="-an -c:v libsvtav1 -preset 5 -g 60 -pix_fmt yuv420p10le -svtav1-params tune=0:scd=0:enable-overlays=1 $C"
> H="-an -c:v libx265 -preset medium -tag:v hvc1 -pix_fmt yuv420p $C -movflags +faststart -x265-params keyint=60:min-keyint=60:scenecut=0"
> X="-an -c:v libx264 -profile:v high -preset slow -tune film -g 60 -keyint_min 60 -sc_threshold 0 -pix_fmt yuv420p $C -movflags +faststart"
> P="crop=850:1512:919:0"; S="scale=1920:1080:flags=lanczos"
> ffmpeg -i master.mp4 $A -crf 36 juno-1512.webm;          ffmpeg -i master.mp4 $H -crf 26 juno-1512-hevc.mp4
> ffmpeg -i master.mp4 -vf $S $A -crf 34 juno-1080.webm;   ... -vf $S $H -crf 25 juno-1080-hevc.mp4;   ... -vf $S $X -crf 24 juno-1080.mp4
> ffmpeg -i master.mp4 -vf $P $A -crf 34 juno-portrait.webm; ... -vf $P $H -crf 26 juno-portrait-hevc.mp4; ... -vf $P $X -crf 25 juno-portrait.mp4
> ffmpeg -i master.mp4 -frames:v 1 -vf "scale=in_range=tv:out_range=pc:in_color_matrix=bt709,format=rgb24" poster_src.png
> ```
> Posters: frame 0 of the graded loop. Pillow 12.3, LANCZOS: 1280x720 and 768x432 (AVIF q58, WebP q72, JPEG q84 progressive),
> plus the portrait crop (919,0)-(1769,1512) at 608x1080.
>
> | File | Codec | Dims | Bytes |
> |---|---|---|---|
> | juno-1512.webm | AV1 Main 10-bit | 2688x1512 | 9,824,386 |
> | juno-1512-hevc.mp4 | HEVC Main (hvc1) | 2688x1512 | 11,217,014 |
> | juno-1080.webm | AV1 Main 10-bit | 1920x1080 | 7,146,228 |
> | juno-1080-hevc.mp4 | HEVC Main | 1920x1080 | 7,993,051 |
> | juno-1080.mp4 | H.264 High | 1920x1080 | 10,844,941 |
> | juno-portrait.webm | AV1 Main 10-bit | 850x1512 | 4,441,094 |
> | juno-portrait-hevc.mp4 | HEVC Main | 850x1512 | 4,562,925 |
> | juno-portrait.mp4 | H.264 High | 850x1512 | 6,178,425 |
> | juno-poster-1280 .avif / .webp / .jpg | | 1280x720 | 65,805 / 61,142 / 149,092 |
> | juno-poster-768 .avif / .webp / .jpg | | 768x432 | 26,879 / 25,782 / 57,680 |
> | juno-poster-portrait .avif / .webp / .jpg | | 608x1080 | 44,325 / 42,152 / 100,479 |

---

# Earlier hero: the coastline clip (Oct 16, 2026; history)

> **Encode of Oct 16, 2026: the coastline clip.** The owner replaced the Jupiter Inlet sunset with a daytime
> drone shot along the Singer Island / Riviera Beach shoreline (turquoise water, condo towers, the Intracoastal behind).
> Everything below the first rule describes the earlier Jupiter Inlet encodes and is kept for history.
>
> - Source: the owner's second upload of `DJI_20261013234059_0426_D_1.mov` (Oct 16, later in the day), 1280x720 H.264 High
>   (yuv420p), bt709 tv range, 29.97 fps, 556 frames (18.55 s), 17,860,760 bytes at 7.4 Mb/s, no audio,
>   sha256 `bc10600f418231c178a250582a19e09e4cef5789cf9f307e2f820e7a2f906b43`. The first upload was the same shot as a
>   2.2 Mb/s HEVC export (sha256 `4663408e…`); this one is cleaner so the set was re-encoded from it.
>   **Both are 720p exports, not the camera original.** If the 4K file from the drone turns up, re-run the commands
>   below on it and the 1440/2160 sets come back.
> - No trim, no dissolve, no grade: the whole shot loops with a plain cut (same as the previous encode).
> - Because the source is 720p there is one landscape set; content.py points `hd` at it and pages.py hands the same
>   set to main.js for `uhd` and `qhd`, so the script is unchanged and a 4K master can be dropped in later.
> - Portrait phones get a 406x720 centre-right crop (`crop=406:720:618:0`), chosen so the towers stay in frame from the
>   first frame to the last as the drone drifts right.
>
> ```sh
> C="-color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv"
> A="-an -c:v libsvtav1 -preset 5 -g 60 -pix_fmt yuv420p10le -svtav1-params tune=0:scd=0:enable-overlays=1 $C"
> H="-an -c:v libx265 -preset medium -tag:v hvc1 -pix_fmt yuv420p $C -movflags +faststart -x265-params keyint=60:min-keyint=60:scenecut=0"
> X="-an -c:v libx264 -profile:v high -preset slow -tune film -g 60 -keyint_min 60 -sc_threshold 0 -pix_fmt yuv420p $C -movflags +faststart"
> P="crop=406:720:618:0"
> ffmpeg -i SRC $A -crf 32 coast-720.webm;   ffmpeg -i SRC $H -crf 24 coast-720-hevc.mp4;   ffmpeg -i SRC $X -crf 23 coast-720.mp4
> ffmpeg -i SRC -vf "$P" $A -crf 32 coast-portrait.webm;  ... $H -crf 24 coast-portrait-hevc.mp4;  ... $X -crf 23 coast-portrait.mp4
> ffmpeg -i SRC -frames:v 1 -vf "scale=in_range=tv:out_range=pc:in_color_matrix=bt709,format=rgb24" poster_src.png
> ```
> Posters: frame 0 of the source. Pillow 12.3: 1280x720 as is and LANCZOS to 768x432 (AVIF q55-60, WebP q70-72,
> JPEG q84 progressive), plus the portrait crop at 406x720. `poster-lqip.txt` is the 32x18 blurred WebP data URI.
>
> | File | Codec | Dims | Duration | Bytes |
> |---|---|---|---|---|
> | coast-720.webm | AV1 Main 10-bit | 1280x720 | 18.55 s (556 f) | 3,999,015 |
> | coast-720-hevc.mp4 | HEVC Main (hvc1) | 1280x720 | 18.55 s | 3,901,830 |
> | coast-720.mp4 | H.264 High | 1280x720 | 18.55 s | 5,232,048 |
> | coast-portrait.webm | AV1 Main 10-bit | 406x720 | 18.55 s | 1,139,382 |
> | coast-portrait-hevc.mp4 | HEVC Main | 406x720 | 18.55 s | 1,003,544 |
> | coast-portrait.mp4 | H.264 High | 406x720 | 18.55 s | 1,481,530 |
> | coast-poster-1280 .avif / .webp / .jpg | | 1280x720 | | 70,867 / 67,352 / 150,032 |
> | coast-poster-768 .avif / .webp / .jpg | | 768x432 | | 25,033 / 30,984 / 64,193 |
> | coast-poster-portrait-720 .avif / .webp / .jpg | | 406x720 | | 18,723 / 22,902 / 51,775 |

---

# Earlier hero: Jupiter Inlet sunset (history)

> **Current encode (Oct 14, 2026): from the 4K original, full clip, no crossfade.** The owner found the
> 1080p crossfade loop blurry (the 1.25 s dissolve doubles the jetty, and AV1 crf 42 smeared the water).
> The sections below the line describe the older 1440p loop and are kept for history.
>
> - Source: Dropbox `/Nicholas Kashuba/kashuba/Jupiter Inlet Sunset.mov`, 3840x2160 H.264, 50.8 Mb/s,
>   23.976 fps, 444 frames (18.52 s), sha256 `0f6d4909465c97083dd37b76caf3a81900d0f7015fc0df3da14d90f3c38e88c6`.
> - No trim, no dissolve, no grade: the whole shot loops with a plain cut. The CSS `filter` on `.hero-media`
>   adds the saturation.
> - main.js picks a set by the device pixels the film fills: > 2400 → 2160p, > 1600 → 1440p, else 1080p;
>   portrait screens get the 1080x1920 crop. Each set lists AV1 webm, then HEVC mp4 (Safari), then H.264.
>
> ```sh
> C="-color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv"
> A="-an -c:v libsvtav1 -preset 5 -g 48 -pix_fmt yuv420p10le -svtav1-params tune=0:scd=0:enable-overlays=1 $C"
> H="-an -c:v libx265 -preset medium -tag:v hvc1 -pix_fmt yuv420p $C -movflags +faststart -x265-params keyint=48:min-keyint=48:scenecut=0"
> X="-an -c:v libx264 -profile:v high -preset slow -tune film -g 48 -keyint_min 48 -sc_threshold 0 -pix_fmt yuv420p $C -movflags +faststart"
> P="crop=1215:2160:1312:0,scale=1080:1920:flags=lanczos"
> ffmpeg -i SRC -vf "$P" $A -crf 36 inlet-portrait.webm;  ffmpeg -i SRC -vf "$P" $H -crf 26 inlet-portrait-hevc.mp4;  ffmpeg -i SRC -vf "$P" $X -crf 26 inlet-portrait.mp4
> ffmpeg -i SRC -vf scale=1920:1080:flags=lanczos $A -crf 36 inlet-1080.webm;  ... $H -crf 26 inlet-1080-hevc.mp4;  ... $X -crf 26 inlet-1080.mp4
> ffmpeg -i SRC -vf scale=2560:1440:flags=lanczos $A -crf 38 inlet-1440.webm;  ... $H -crf 27 inlet-1440-hevc.mp4
> ffmpeg -i SRC $A -crf 38 inlet-2160.webm
> ```
> Posters: frame 0 of the source, Pillow LANCZOS to 2560/1920/1280/768 wide (AVIF q50-60, WebP q70-72, JPEG q84)
> and the portrait crop (1312,0)-(2527,2160) to 1080x1920. At crf 36-40 the AV1 frames matched the source
> side by side on the water and jetty; the source itself is soft drone footage.

---

## Source

- Dropbox: `/Nicholas Kashuba/kashuba/Jupiter Inlet Sunset-1440p.mp4`
- sha256: `fa46ae4f0a6a3fa04f68c431c27041285311b9a162749dff10b90127de29db06`
- 2560x1440 H.264, yuv420p, bt709, 24000/1001 fps, 444 frames (18.42 s), 14,350,328 bytes, **no audio stream**
- The source is NOT committed to this repo. Fetch it from Dropbox to re-encode.

## What the footage is

One continuous drone shot with no cuts. The drone slowly orbits/yaws over the Jupiter Inlet mouth. At t=0 it looks
NW with the Atlantic and the Jupiter/Tequesta beach on the right, the south jetty curling into the
frame center-right, and the sun low at the upper left. By t=18 it has swung around to look straight up
the inlet channel into the sun, which sits near the top center. The horizon stays level at about 25% from the top for the
whole shot. Exposure is locked: per-frame mean luma 112.1–114.8 (8-bit), largest frame-to-frame delta 0.5.
There are no exposure snaps or glitches. The motion speeds up slightly over the shot (frame-diff energy 4.4 to 7.3).
The source sky is already clipped in the red channel (about 60% of pixels in the top band at 255) but never clips in all channels.

## Loop design (all timestamps on the source)

- Trim window: source frames **0–335** (0.000 s – 14.014 s).
- Crossfade length X = **30 frames (1.251 s)**.
- body = frames 30–335 (1.251 s – 14.014 s, 306 frames); head = frames 0–29 (0.000 – 1.210 s).
- `xfade=fade` blends the last 30 frames of body (source 12.763–14.014 s) into the head, so the output
  **ends on source frame 29 and starts on source frame 30**. The wrap is a normal one-frame step:
  luma mean-abs-diff at the wrap is 1.89, against 1.1–2.35 for ordinary consecutive frames.
- Output: **306 frames = 12.763 s** at 23.976 fps.
- Why this window: the orbit only goes one way, so head and tail views can never match. I searched every
  (start, end) pair with a 12.5–15.5 s span. The best match is at the very start of the clip, where motion is slowest
  (diff 28 vs 32–40 for later windows). Because the horizon and sky band stay registered, the 1.25 s dissolve reads
  as a soft cross-dissolve of the land only. 0.8 s looked like a visible "pop" of double jetties, so I used 1.25 s.
- Speed: native (no setpts). The orbit is already slow and calm. Slowing it with setpts would either drop to
  about 21 fps (judder on pans) or need motion interpolation (artifacts on water and surf).

## Grade

Kept light so the sunset stays natural:
`curves=all='0/0 0.25/0.235 0.5/0.485 0.8/0.795 1/1',eq=saturation=1.06`.
This adds slight density in the lower mids (helps the left/bottom text scrim) and +6% saturation. Highlights are untouched, so the clip
fraction is unchanged (G≥250: 5.6%, R≥250: 12.8% on frame 0). Mean RGB on frame 0 went from 110/113/103 to 106/111/97.

## Portrait crop

`crop=810:1440:875:0` (9:16, centered, x offset **875 px** on the 2560-wide source), scaled to 720x1280.
I checked offsets 640, 875 and 1100 across the loop. 875 keeps the south jetty tip and the inlet channel in frame from
start to end. 640 loses the jetty late in the loop, and 1100 loses it early.

## Commands

Work dir: scratch (`.../scratchpad/video/work`). `SRC=inlet-1440.mp4`.

```sh
# 1. Loop master (near-lossless, ungraded)
ffmpeg -i $SRC -filter_complex "[0:v]split[a][b];\
[a]trim=start_frame=30:end_frame=336,setpts=PTS-STARTPTS[body];\
[b]trim=start_frame=0:end_frame=30,setpts=PTS-STARTPTS[head];\
[body][head]xfade=transition=fade:duration=1.2513:offset=11.5115,format=yuv420p[v]" \
 -map "[v]" -an -c:v libx264 -preset slow -crf 8 \
 -color_primaries bt709 -color_trc bt709 -colorspace bt709 master_ungraded.mp4

# 2. Graded lossless mezzanine
ffmpeg -i master_ungraded.mp4 -vf "curves=all='0/0 0.25/0.235 0.5/0.485 0.8/0.795 1/1',eq=saturation=1.06,format=yuv420p" \
 -c:v ffv1 -level 3 -an mezz.mkv

# Common flags
X="-an -c:v libx264 -profile:v high -preset veryslow -tune film -g 48 -keyint_min 48 -sc_threshold 0 -pix_fmt yuv420p \
   -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -movflags +faststart"
A="-an -c:v libsvtav1 -preset 5 -g 48 -pix_fmt yuv420p10le -svtav1-params tune=0:enable-overlays=1:scd=0 \
   -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv"
P="crop=810:1440:875:0,scale=720:1280:flags=lanczos"

# 3. Renditions
ffmpeg -i mezz.mkv -vf scale=1920:1080:flags=lanczos $X -crf 29 inlet-1080.mp4
ffmpeg -i mezz.mkv -vf scale=1280:720:flags=lanczos  $X -crf 28 inlet-720.mp4
ffmpeg -i mezz.mkv -vf "$P"                          $X -crf 28 inlet-portrait.mp4
ffmpeg -i mezz.mkv -vf scale=1920:1080:flags=lanczos $A -crf 42 inlet-1080.webm
ffmpeg -i mezz.mkv -vf scale=1280:720:flags=lanczos  $A -crf 44 inlet-720.webm
ffmpeg -i mezz.mkv -vf "$P"                          $A -crf 42 inlet-portrait.webm

# 4. Poster sources = frame 0 of the graded loop (identical to the first video frame)
ffmpeg -i mezz.mkv -frames:v 1 -vf "scale=in_range=tv:out_range=pc:in_color_matrix=bt709,format=rgb24" poster_src.png
ffmpeg -i mezz.mkv -frames:v 1 -vf "crop=810:1440:875:0,scale=in_color_matrix=bt709,format=rgb24" poster_por_src.png
```

Posters (Pillow 12.3 with native AVIF support, LANCZOS resize):

```python
r = src.resize((w, h), Image.LANCZOS)
r.save(f"{name}.avif", quality=AQ, speed=4)      # AQ: 1920→46, 1280/768→55, portrait→50
r.save(f"{name}.webp", quality=WQ, method=6)     # WQ: 62 (landscape), 58 (portrait)
r.save(f"{name}.jpg", quality=78, progressive=True, optimize=True, subsampling="4:2:0")
# LQIP: 32x18, GaussianBlur(1), WebP q50 → data URI in poster-lqip.txt
```

Tuning notes: the water texture is expensive. x264 1080 crf 27 = 5.78 MB, crf 29 = 4.40 MB (chosen), crf 30 = 3.83 MB.
AV1 1080 crf 40 = 4.02 MB in 1m50s on 4 cores (preset 5), crf 42 = 3.53 MB (chosen). AV1 720 crf 42 = 1.93 MB was over target, so it uses crf 44.
AV1 is 10-bit Main profile to avoid banding in the sky gradient; every AV1 hardware/software decoder supports Main 10-bit.

## Outputs

| File | Codec | Dims | Duration | Bytes |
|---|---|---|---|---|
| inlet-1080.mp4 | H.264 High, yuv420p | 1920x1080 | 12.763 s (306 f) | 4,396,499 |
| inlet-1080.webm | AV1 Main, 10-bit | 1920x1080 | 12.763 s | 3,533,578 |
| inlet-720.mp4 | H.264 High | 1280x720 | 12.763 s | 2,478,638 |
| inlet-720.webm | AV1 Main, 10-bit | 1280x720 | 12.763 s | 1,706,706 |
| inlet-portrait.mp4 | H.264 High | 720x1280 | 12.763 s | 2,415,327 |
| inlet-portrait.webm | AV1 Main, 10-bit | 720x1280 | 12.763 s | 1,756,496 |
| inlet-poster-1920.avif / .webp / .jpg | | 1920x1080 | | 76,317 / 112,520 / 251,733 |
| inlet-poster-1280.avif / .webp / .jpg | | 1280x720 | | 62,117 / 61,390 / 128,779 |
| inlet-poster-768.avif / .webp / .jpg | | 768x432 | | 25,428 / 25,026 / 51,071 |
| inlet-poster-portrait-720.avif / .webp / .jpg | | 720x1280 | | 43,903 / 50,826 / 119,456 |
| poster-lqip.txt | WebP data URI | 32x18 | | 223 chars |

None of the videos has an audio track. All are tagged bt709 / tv range, keyframes every 48 frames (2 s), and every MP4 has its moov atom before mdat (faststart).

## Re-encode from source

1. Download the Dropbox file above and check its sha256.
2. Run steps 1–4 above in order. Every later step reads `mezz.mkv`, so a grade change only needs step 2 onward.
3. To change the loop, change `start_frame`/`end_frame` and recompute `offset = (body_frames − X_frames) / 23.976`
   and `duration = X_frames / 23.976`. Check the wrap by comparing the last and first output frames.
