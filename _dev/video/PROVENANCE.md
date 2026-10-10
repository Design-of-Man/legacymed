# Hero video: Jupiter Inlet sunset

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
