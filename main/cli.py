res_str = input("Numerical resolution (Higher values use more numbers for higher detail. Default=512): ")
res = 512
if len(res_str)!=0:
    res = int(res_str)
scale_str = input("Scale (The scale of the output image, makes the image higher resolution, NOT UPSCALING. Default=5): ")
scale = 5
if len(scale_str)!=0:
    scale = int(scale_str)