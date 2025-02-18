'''
Write the program "99 Bottles of Beer on the Wall" using a while loop. 
Be mindful to change the word 'bottles' to 'bottle' when down to the last one. 
You must do the full 99 bottles; the sample shows the last 3 verses.
'''
# Variable storing the count of beer bottles
beer_count = 99

# While beer_count is greater than 2, it'll keep printing -1 bottle each time.
while beer_count > 2:
    print(f"{beer_count} bottles of beer on the wall \n{beer_count} bottles of beer \nTake one down, pass it around")
    beer_count -= 1
    print(f"{beer_count} bottles of beer on the wall!\n\n")

# The last two print sections take into consideration the grammar of one beer bottle and no beer bottles after it is done.
print(f"{beer_count} bottles of beer on the wall \n{beer_count} bottles of beer \nTake one down, pass it around")
beer_count -= 1
print(f"1 bottle of beer on the wall!\n\n")

print(f"{beer_count} bottle of beer on the wall \n{beer_count} bottle of beer \nTake one down, pass it around")
beer_count -= 1
print(f"No bottles of beer on the wall!\n\n")
