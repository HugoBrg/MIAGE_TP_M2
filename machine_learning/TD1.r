  #----------------------------------------------#
# DOWNLOADING AND INSTALLING REQUIRED PACKAGES #
#----------------------------------------------#

# Install packages (will update them if already installed)
install.packages("rvest")
install.packages("ggplot2")
install.packages("dplyr")
install.packages("scales")
install.packages("maps")
install.packages("mapproj")
install.packages("plotly")

# Activate packages
library(rvest)
library(ggplot2)
library(dplyr)
library(scales)
library(maps)
library(mapproj)
library(plotly)

#---------------------------------#
# DOWNLOADING DATA FROM WIKIPEDIA #
#---------------------------------#

# The read_html() function load the web page html content in an object named le
le = read_html("https://en.wikipedia.org/w/index.php?title=List_of_U.S._states_and_territories_by_life_expectancy&oldid=928537169")

# Filter html content inobject le to keep only the life expectancy table
le = le %>% html_nodes("table") %>% .[[2]] %>% html_table(fill=T)
View(le)

#--------------------#
# DATA PREPROCESSING #
#--------------------#

# Column selection
le = le[c(1,2,6,7)]
View(le)

# Renaming columns ('le' : life expectancy)
names(le)[c(3,4)] = c("le_caucasian", "le_african")
View(le)

# Converting to numerical format (encodes missing values with NAs)
le$le_caucasian <- as.numeric(le$le_caucasian)
le$le_african <- as.numeric(le$le_african)
View(le)

# Calculating Differences Between Caucasian-American and African-American Life Expectancy 
le$le_diff = le$le_caucasian - le$le_african
View(le)

# Loading USA states data
states = map_data("state")

# Creating a new variable 'region' with state names 
le$region = tolower(le$State)
View(le)

# Merging our data with the USA 'states' data from 'maps' package
states = merge(states, le, by="region", all.x=T)

#---------------------------------------#
# DISPLAYING DATA ON THE MAP OF THE USA #
#---------------------------------------#

# For correctly displaying accentuated characters in maps
options(encoding="latin1")

# Life expectancy of African-Americans
ggplot(states, aes(x = long, y = lat, group = group, fill = le_african)) + geom_polygon(color = "white") + scale_fill_gradient(name = "Years", low = "#ffe8ee", high = "#c81f49", guide = "colorbar", na.value="#eeeeee") + labs(title="Esp�rance de vie du groupe ethnique Afro-Am�ricain") + coord_map()

# Life expectancy of Caucasian-American
ggplot(states, aes(x = long, y = lat, group = group, fill = le_caucasian)) + geom_polygon(color = "white") + scale_fill_gradient(name = "Years", low = "#ffe8ee", high = "#c81f49", guide = "colorbar", na.value="Gray") + labs(title="Esp�rance de vie du groupe ethnique Caucasien-Am�ricain") + coord_map()

# Dipslay differencies between life expectancies
ggplot(states, aes(x = long, y = lat, group = group, fill = le_diff)) + geom_polygon(color = "white") + scale_fill_gradient(name = "Years", low = "#ffe8ee", high = "#c81f49", guide = "colorbar", na.value="#eeeeee") + labs(title="Diff�rences dans l'esp�rance de vie des groupes ethniques \nCaucasien et Afro-Am�ricain par �tat aux USA") + coord_map()

# Display interactive USA map with contextual message for each state : caucasian-american
map_plot_caucasian = ggplot(states, aes(x = long, y = lat, group = group, fill = le_caucasian)) + geom_polygon(color = "white") + scale_fill_gradient(name = "Years", low = "#ffe8ee", high = "#c81f49", guide = "colorbar", na.value="#eeeeee") + labs(title="Esp�rance de vie du groupe ethnique Caucasien-Am�ricain") + coord_map()
ggplotly(map_plot_caucasian)

# Display interactive USA map with contextual message for each state : afro-american
map_plot_african = ggplot(states, aes(x = long, y = lat, group = group, fill = le_african)) + geom_polygon(color = "white") + scale_fill_gradient(name = "Years", low = "#ffe8ee", high = "#c81f49", guide = "colorbar", na.value="#eeeeee") + labs(title="Esp�rance de vie du groupe ethnique Afro-Am�ricain") + coord_map()
ggplotly(map_plot_african)
