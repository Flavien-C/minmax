reset
set terminal png
set output "graph2.png"
set key outside
set key right box
set title "Nombre de noeuds explorés en fonction\n de la probabilité de créer des liens\n entre machines"
set grid
set xlabel "Probabilité"
set ylabel "Noeuds explorés"
plot "data2.dat" using 1:2 with linespoints lc rgb "#0000FF" lw 2 title "minimax moyenne",\
    "data2.dat" using 1:3 with linespoints lc rgb "#FF0000" lw 2 title "alphabeta moyenne"