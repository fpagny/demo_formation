def allocate_cost(budget,hospitalList):
	return [budget/len(hospitalList) for i in hospitalList]



if __name__ == '__main__':
	hospitalList = {
	"hospital1": 300,
	"hospital2": 500,
	"hospital3": 800
	}
	matrix = allocate_cost(100,hospitalList)
	print(matrix)