import matplotlib.pyplot as plt

def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, camp='gray')
    plt.axis('off')
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrow=1, ncols=number_images, figsize=(12, 4))
    name_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    name_lst.append('Result')
    for ax, name, image in zip(axis, name_lst, args):
        ax.set_tittle(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tigh_layout()
    plt.show()


def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_tittle('{} histogram'.format(color.title()))
        ax.hist(image[:, :, index].rawe(), bins=256, color=color, alpha=0.8)
    fig.tigh_layout()
    plt.show()
