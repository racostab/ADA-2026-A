
#include <iostream>
#include <fstream>
#include <cstdlib>

int main() {
    // ---- Datos ----
    int n[]    = {5, 10, 20, 50, 100, 200, 300, 500, 750, 1000};
    double tH[] = {0.00649078, 0.00671208, 0.00253657, 0.00252211,
                   0.00433407, 0.01184408, 0.02389706, 0.06173543,
                   0.13645960, 0.23618338};
    double tM[] = {0.00640803, 0.00658807, 0.00239841, 0.00281860,
                   0.00425649, 0.01200832, 0.02314998, 0.06077866,
                   0.13069152, 0.24335914};
    int sz = sizeof(n) / sizeof(n[0]);

    // ---- Escribir datos a archivo ----
    std::ofstream datos("datos_tiempos.dat");
    datos << "# n  tiempo_H  tiempo_M\n";
    for (int i = 0; i < sz; i++) {
        datos << n[i] << "  " << tH[i] << "  " << tM[i] << "\n";
    }
    datos.close();

    // ---- Script Gnuplot ----
    std::ofstream gp("grafica.gp");
    gp << "set terminal pngcairo size 900,600 enhanced font 'Arial,12'\n";
    gp << "set output 'graph_C++.png'\n";
    gp << "\n";
    gp << "set title 'Gráfica de n entradas respecto al tiempo C++' font 'Arial Bold,14'\n";
    gp << "set xlabel 'n (Entradas)'\n";
    gp << "set ylabel 'Tiempo'\n";
    gp << "set grid\n";
    gp << "set key top left\n";
    gp << "\n";
    gp << "set style line 1 lc rgb '#0072BD' lw 2 pt 7 ps 1.2\n";
    gp << "set style line 2 lc rgb '#D95319' lw 2 pt 9 ps 1.2\n";
    gp << "\n";
    gp << "plot 'datos_tiempos.dat' using 1:2 with linespoints ls 1 title 'Hombres proponen', \\\n";
    gp << "     'datos_tiempos.dat' using 1:3 with linespoints ls 2 title 'Mujeres proponen'\n";
    gp.close();

    // ---- Ejecutar Gnuplot ----
    int ret = system("gnuplot grafica.gp");
    if (ret == 0) {
        std::cout << "Grafica generada: grafica_tiempos.png\n";
    } else {
        std::cerr << "Error al ejecutar gnuplot. Asegurate de tenerlo instalado.\n";
        return 1;
    }

    return 0;
}


/*

#include <iostream>
#include <fstream>
#include <cstdlib>

int main() {
    // ---- Datos ----
    int n[]     = {5, 10, 20, 50, 100, 200, 300, 500, 750, 1000};
    double tH[] = {0.02160344, 0.03087964, 0.03063197, 0.02323091,
                   0.02689090, 0.05682086, 0.10287255, 0.26202362,
                   0.63979212, 1.22003812};
    double tM[] = {0.02215418, 0.02306263, 0.02511537, 0.03443901,
                   0.03182563, 0.05704028, 0.10380120, 0.26334030,
                   0.65030691, 0.97844313};
    int sz = sizeof(n) / sizeof(n[0]);

    // ---- Escribir datos a archivo ----
    std::ofstream datos("datos_tiempos2.dat");
    datos << "# n  tiempo_H  tiempo_M\n";
    for (int i = 0; i < sz; i++) {
        datos << n[i] << "  " << tH[i] << "  " << tM[i] << "\n";
    }
    datos.close();

    // ---- Script Gnuplot ----
    std::ofstream gp("grafica2.gp");
    gp << "set terminal pngcairo size 900,600 enhanced font 'Arial,12'\n";
    gp << "set output 'graph_Python.png'\n";
    gp << "\n";
    gp << "set title 'Gráfica de n entradas respecto al tiempo Python' font 'Arial Bold,14'\n";
    gp << "set xlabel 'n (Entradas)'\n";
    gp << "set ylabel 'Tiempo'\n";
    gp << "set grid\n";
    gp << "set key top left\n";
    gp << "\n";
    gp << "set style line 1 lc rgb '#0072BD' lw 2 pt 7 ps 1.2\n";
    gp << "set style line 2 lc rgb '#D95319' lw 2 pt 9 ps 1.2\n";
    gp << "\n";
    gp << "plot 'datos_tiempos2.dat' using 1:2 with linespoints ls 1 title 'Hombres proponen', \\\n";
    gp << "     'datos_tiempos2.dat' using 1:3 with linespoints ls 2 title 'Mujeres proponen'\n";
    gp.close();

    // ---- Ejecutar Gnuplot ----
    int ret = system("gnuplot grafica2.gp");
    if (ret == 0) {
        std::cout << "Grafica generada: grafica_tiempospython.png\n";
    } else {
        std::cerr << "Error al ejecutar gnuplot. Asegurate de tenerlo instalado.\n";
        return 1;
    }

    return 0;
}
*/
