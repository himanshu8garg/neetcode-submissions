class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(mat1)):
            result.append([0]*len(mat2[0]))


        for row_index, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                # if row_element:
                    for col_index, col_element in enumerate(mat2[element_index]):
                        result[row_index][col_index] += row_element * col_element
        
        
        return result
            

