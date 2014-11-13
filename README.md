blendswap-uploader
==================

A Blender Addon to easily share your blend on Blend Swap, directly from Blender.

## Project goals:

+ An easy to use, quick addon that will share your blend on Blend Swap.
+ Client side blend file checklist:
  + Are all texture and other media files packed?
  + Capture 3 orthogonal views and one perspective of the viewport inside of blender (with edges visible) and save them to hard drive.
  + Render a preview image with nice and quick settings and save it to hard drive.
  + Prepare a folder or package for uploading.
  + Ask the user for all data to be added to the blend's page.
  + Encode to base64 and send to https://www.blendswap.com/blends/add server using the user's credentials (using HTTPS only).
  + Wait for response and inform of completion status, if possible, with upload percentage.
  + Offer a link to the blend when completed or a failure notice upon error.

In the future this can become the base for a Blend Swap browser inside of Blender since Blend Swap 5.5+ will offer a basic open json API (mostly for GET requests). We'll see how that plays out.

All contributions are welcome! Please clone this repository and submit your pull requests for review.
