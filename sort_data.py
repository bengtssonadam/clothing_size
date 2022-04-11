import pandas as pd


def create_tshirts(gender):

    df = pd.read_csv(gender +'.csv')

    chests = [c/10 for c in df.chestcircumference.tolist()]
    waists = [w/10 for w in df.waistcircumference.tolist()]
    heights = [w / 10 for w in df.stature.tolist()]
    weights = [w / 10 for w in df.weightkg.tolist()]

    with open(gender + '_clean_tshirt.csv', 'w') as outfile:
        outfile.write('height,weight,size\n')

        for i in range(len(chests)):
            chest = chests[i]
            waist = waists[i]

            sizes = {
                1: 'xs',
                2: 's',
                3: 'm',
                4: 'l',
                5: 'xl'
            }

            chest_size = 0

            if chest < 87:
                chest_size = 1
            elif 87 <= chest < 93:
                chest_size = 2
            elif 93 <= chest < 99:
                chest_size = 3
            elif 99 <= chest < 105:
                chest_size = 4
            else:
                chest_size = 5

            waist_size = 0
            if waist < 75:
                waist_size = 1
            elif 75 <= waist < 81:
                waist_size = 2
            elif 81 <= waist < 87:
                waist_size = 3
            elif 87 <= waist < 93:
                waist_size = 4
            else:
                waist_size = 5

            size = max(chest_size, waist_size)
            size_str = sizes[size]
            outfile.write(f'{heights[i]},{weights[i]},{size_str}\n')


def main():
    pass
    # create_tshirts('male')
    # create_tshirts('female')


if __name__ == '__main__':
    main()
