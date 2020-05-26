# pypaintsearch
Use OCR to Search Warhammer Paint Shelf at Local Game Shop

## The Problem
There's a shelf of paints at a game store near me. It takes too long to find
a paint by name. I'm going to attempt to use OCR to get the locations of the
paints in an image, and then use that data to create a simple webapp that can
help me locate a color on the rack.

## To Do
* Create Image to Scan - Put the source images into one large image, with one
layer being the photo of the entire rack, and another layer being the
collected images with enough definition for OCR.
* Generate Name-Location Data - Use OCR to get the location of paint names in
the large image.
* Web App - Create simple web page to search for the location of a paint.
