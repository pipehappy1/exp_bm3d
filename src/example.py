import bm3d
import imageio
import numpy as np
import sewar


background_noise = "/home/yguan/data/SI/CUT_CH1_no_signal/test02978_x13020_y17820_w512_h512.tif"
img_noisy = imageio.imread(background_noise)
print("background_noise get shape of {}, dtype: {}".format(img_noisy.shape, img_noisy.dtype))

img_noisy = img_noisy[:256,:256]

foreground = "/home/yguan/data/Spatial_Envelope/spatial_envelope_256x256_static_8outdoorcategories/insidecity_hous114.jpg"
img_fore = imageio.imread(foreground)
print("foreground_noise get shape of {}, dtype: {}".format(img_fore.shape, img_fore.dtype))

raw = img_fore.astype(np.float)
img_fore = (raw[:256,:256,0] + raw[:256,:256,0] + raw[:256,:256,0])/3

tlambda = 0.1

combined = img_noisy.astype(np.float) * tlambda + img_fore.astype(np.float)
print("max: {}, min: {}".format(combined.max(), combined.min()))

combined = (combined - combined.min())/(combined.max() - combined.min())
print("max: {}, min: {}".format(combined.max(), combined.min()))

clean = (img_fore - combined.min())/(combined.max() - combined.min())

img_denoised = bm3d.bm3d(combined, sigma_psd=30/255, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)

psnr = sewar.full_ref.psnr((clean*255).astype(np.uint8), (img_denoised*255).astype(np.uint8))
ssim = sewar.full_ref.ssim((clean*255).astype(np.uint8), (img_denoised*255).astype(np.uint8))

print("psnr: {}, ssim: {}".format(psnr, ssim))

imageio.imwrite('denoised.png', img_denoised)
imageio.imwrite('clean.png', clean)



