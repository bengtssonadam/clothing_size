import pandas as pd


def create_size_tshirts(gender):

    df = pd.read_csv(gender +'.csv')

    chests = [c/10 for c in df.chestcircumference.tolist()]
    waists = [w/10 for w in df.waistcircumference.tolist()]
    heights = [w / 10 for w in df.stature.tolist()]
    weights = [w / 10 for w in df.weightkg.tolist()]

    with open(gender + 'tshirt.csv', 'w') as outfile:
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


def create_size_pants(gender):

    df = pd.read_csv(gender +'.csv')


    legheights = [c/10 for c in df.crotchheight.tolist()]
    waists = [w/10 for w in df.waistcircumference.tolist()]
    heights = [w / 10 for w in df.stature.tolist()]
    weights = [w / 10 for w in df.weightkg.tolist()]

    with open(gender + 'pants.csv', 'w') as outfile:
        outfile.write('height,weight,size\n')

        for i in range(len(waists)):
            legheight = legheights[i]
            waist = waists[i]

            sizes = {
                1: 'xs',
                2: 's',
                3: 'm',
                4: 'l',
                5: 'xl'
            }

            legheight_size = 0

            if gender == 'female':
                if legheight < 79:
                    legheight_size = 1
                elif 79 <= legheight < 80.5:
                    legheight_size = 2
                elif 80.5 <= legheight < 82:
                    legheight_size = 3
                elif 82 <= legheight < 83.5:
                    legheight_size = 4
                else:
                    legheight_size = 5

                waist_size = 0
                if waist < 64:
                    waist_size = 1
                elif 64 <= waist < 70:
                    waist_size = 2
                elif 70 <= waist < 76:
                    waist_size = 3
                elif 76 <= waist < 82:
                    waist_size = 4
                else:
                    waist_size = 5

            else:
                if legheight < 82:
                    legheight_size = 1
                elif 82 <= legheight < 84:
                    legheight_size = 2
                elif 84 <= legheight < 86:
                    legheight_size = 3
                elif 86 <= legheight < 88:
                    legheight_size = 4
                else:
                    legheight_size = 5

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

            size = max(legheight_size, waist_size)
            size_str = sizes[size]
            outfile.write(f'{heights[i]},{weights[i]},{size_str}\n')


def main():
    create_size_pants('male')
    create_size_pants('female')
    create_size_tshirts('male')
    create_size_tshirts('female')


if __name__ == '__main__':
    main()
