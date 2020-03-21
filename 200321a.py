import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def main():
    img_path = "/Users/xanonymous/Downloads/90176421_169661774005231_9103801027802431488_n.jpg"
    img = mpimg.imread(img_path).copy()
    for row in img:
        for col in row:
            if col[0] > col[1] and col[0] > col[2] and (col[1] - col[2] < 25 or col[2] - col[1] < 25):
                col[2] = 0
    plt.imshow(img)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    main()
