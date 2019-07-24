numOfBottles = 99

while True:
    # number of bottles
    if numOfBottles > 0:
        numOfBottlesMinus = numOfBottles - 1
    else:
        numOfBottlesMinus = 99

    # bottle or bottles
    if numOfBottles == 1:
        bottles = "bottle"
        bottlesMinus = "bottles"
    elif numOfBottles == 2:
        bottles = "bottles"
        bottlesMinus = "bottle"
    else:
        bottles = "bottles"
        bottlesMinus = "bottles"

    if numOfBottles == 0:
        print(
            "{num} {bottles} of beer on the wall, {num} {bottles} of beer.\nGo to the store and buy some more, {numMinus} {bottlesMinus} of beer on the wall.".format(
                num=numOfBottles,
                numMinus=numOfBottlesMinus,
                bottles=bottles,
                bottlesMinus=bottlesMinus,
            )
        )
        # break so we don't loop
        break
    else:
        print(
            "{num} {bottles} of beer on the wall, {num} {bottles} of beer.\nTake one down and pass it around, {numMinus} {bottlesMinus} of beer on the wall.".format(
                num=numOfBottles,
                numMinus=numOfBottlesMinus,
                bottles=bottles,
                bottlesMinus=bottlesMinus,
            )
        )

    numOfBottles = numOfBottlesMinus
