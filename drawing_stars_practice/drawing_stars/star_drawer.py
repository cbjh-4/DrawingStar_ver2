class StarDrawer:
    #생성자 alias : 별명, num_lines : 줄 숫자
    def __init__(self, alias = '홍길동', num_lines = 5, drawing_char = '*', drawing_shape = 'shape1'):
        self.alias = alias
        self.num_lines = num_lines
        self.drawing_char = drawing_char
        self.drawing_shape = drawing_shape

#drawing_shape  shpae1:피라미드, shpae2:마름모, shpae3:내림차순, shpae4:오름차순
    def draw_stars(self):
        star_str = f'{self.alias}이(가) 그립니다.\n'
        
        if(self.drawing_shape == 'shape1'):
            for i in range(self.num_lines):
                star_str += ' '*(self.num_lines -i) + self.drawing_char*(i*2+1) + '\n'
            return star_str
        elif(self.drawing_shape == 'shape2'):
            for i in range(self.num_lines):
                star_str += ' '*(self.num_lines -i) + self.drawing_char*(i*2+1) + '\n'            
            for j in range(self.num_lines - 1, 0, -1):
                    star_str += ' ' * (self.num_lines - j + 1) + self.drawing_char * (j * 2 - 1) + '\n'
            return star_str
        elif(self.drawing_shape == 'shape3'):
            for i in range(self.num_lines):
                star_str += ' '*i + self.drawing_char*(self.num_lines-i) + '\n'
            return star_str
        elif(self.drawing_shape == 'shape4'):
            for i in range(self.num_lines):
                star_str += ' '*(self.num_lines-i-1) + self.drawing_char*(i+1) + '\n'
            return star_str
