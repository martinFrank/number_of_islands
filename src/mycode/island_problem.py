import island_parser
import island

#https://leetcode.com/problems/number-of-islands/description/
 
# invoke our function 
csvFile = 'C:\\Users\\m.frank\\IdeaProjects\\privat\\pyIslands\\src\\resources\\island_01.csv'
data = island_parser.read_csv(csvFile)

island_map = island.Map(data)
number_of_islands = island_map.calculate_number_of_islands()
print (f"this map has {number_of_islands} islands")

