def to_smash(total_candies):
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")


print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")