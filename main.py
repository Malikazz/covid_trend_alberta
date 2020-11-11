import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# This just sets up a list of == length to the objects 
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
## then this uses that list to set how many bars we need
## and what their values are
plt.bar(y_pos, performance, align='center', alpha=0.5)
## then this set the names of thoses bars
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.savefig('test.png')