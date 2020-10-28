Run the BM3D for denoising


To setup, there is a post:

    What I resorted to was using the PyPI package, which is advertised here: http://www.cs.tut.fi/~foi/GCF-BM3D/index.html#ref_software.
    
    I dug a bit in the source code, and found that I could perform BM3D, in the following fashion:
    
    import bm3d
    
    denoised_image = bm3d.bm3d(image_noisy, sigma_psd=30/255, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)
    There are also some examples in the library's source code download.
    
    I installed bm3d using pip (pip install bm3d) and needed OpenBlas (sudo apt-get install libopenblas-dev).
