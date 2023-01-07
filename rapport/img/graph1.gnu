reset
set terminal png
set output "graph1.png"
set key outside
set key right box
set title "Nombre de noeuds explorés en fonction\n de la profondeur de recherche"
set grid
set xlabel "Profondeur"
set ylabel "Noeuds explorés"
plot "data1.dat" using 1:2 with linespoints lc rgb "#0000FF" lw 2 title "minimax",\
    "data1.dat" using 1:3 with linespoints lc rgb "#FF0000" lw 2 title "alphabeta"