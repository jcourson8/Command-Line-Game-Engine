# string = """
# ########
# ########
# ########
# #      #
# #      #
# #      #
# #      #
# # 1    #
# #      #
# #      #
# #      #
# ########"""

# print(string,end='\r\r\r')
# print(string)

def get_relative_index(cord, height, border_width):
    x, y = cord
    x = x + border_width
    if y == 0:
        y = height
    else:
        y = ((-(height+border_width) - y) %
             height+border_width) + border_width+3
    return (x, y)


a = get_relative_index((1, 3), 17, 4)
print(a)


#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
