import matplotlib.pyplot as plt
from random import randint as rand
from utils.cache import gen_cache_name
from utils.scienceutils import sort_genotype

async def punnett(g1, g2, size, person):
    offspring = []
    if size == 2:
        x_labels, y_labels = [g1[0], g1[1]], [g2[0], g2[1]]
        for y_label in y_labels:
            offspring.append([sort_genotype([y_label, x_label]) for x_label in x_labels])
    if size == 4:
        x_labels = [g1[0]+g1[2], g1[0]+g1[3], g1[1]+g1[2], g1[1]+g1[3]]
        y_labels = [g2[0]+g2[2], g2[0]+g2[3], g2[1]+g2[2], g2[1]+g2[3]]
        for y_label in y_labels:
            offspring.append([sort_genotype([y_label[0], x_label[0], y_label[1], x_label[1]]) for x_label in x_labels])
    plt.close()
    ps = plt.table(
        colLabels=x_labels,
        rowLabels=y_labels,
        cellText=offspring,
        loc='center'
    )
    ps.auto_set_font_size(False)
    ps.set_fontsize(15)
    ps.scale(1, 3)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)
    plt.title(f"Punnett Square For {g1} x {g2}:")
    plt.xlabel(f"Generated by STEMbot\nFor @{person}")

    im_id = gen_cache_name()
    path = f'./caches/punnett/{im_id}.png'
    plt.savefig(path, bbox_inches='tight', pad_inches=0.5)
    plt.close()
    return path