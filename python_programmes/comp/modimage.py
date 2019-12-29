from PIL import Image


im = Image.open("orig_image.png")
rgb_im = im.convert('RGB')
width, height = im.size

out = Image.new('RGB', (width, height))

for row in range(height):
    for col in range(width):
        r, g, b = rgb_im.getpixel((col, row))
        out.putpixel((col, row),((r+g+b)//3,(r+g+b)//3,(r+g+b)//3 ))

out.save("bandw.png")
out.show()

out.show("This is the title")
