from matplotlib import image as mp_img, pyplot as plt


def to_gray(img):
    img[..., 0] = img[..., 1] = img[..., 2]
    return img


def to_yellow(img):
    for row in img:
        for col in row:
            if col[0] > col[1] and col[0] > col[2] and (col[1] - col[2] < 25 or col[2] - col[1] < 25):
                col[2] = 0
    return img


def main():
    img_path = "/Users/xanonymous/Downloads/90176421_169661774005231_9103801027802431488_n.jpg"
    img = mp_img.imread(img_path).copy()
    plt.imshow(to_yellow(img.copy()))
    plt.axis("off")
    plt.show()
    plt.imshow(to_gray(img.copy()))
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    main()
