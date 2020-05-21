#include <Python.h>
#include <time.h>
#include <stdio.h>
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
		
    int N;
	if(!PyArg_ParseTuple(args, "i", &N)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
    clock_t begin = clock();
    double *X = malloc(N*sizeof(double));
    double *Y = malloc(N*sizeof(double));
    srand(time(NULL));
	for(int i=0; i<N;i++)
    {
        X[i] = rand() / ((double) RAND_MAX);
        Y[i] = rand() / ((double) RAND_MAX);
    }
    double kwadrat[2] = {0.1, 0.1};
    double trafiony = 0;
    double wszystkie = N*10;
    while(kwadrat[0] <= 1)
    {
        for(int i=0;i<N;i++)
        {
            if(X[i] <= kwadrat[0])
            {
                if(Y[i] <= kwadrat[1])
                {
                    trafiony += 1.0;
                }
            }
        }

        kwadrat[0] += 0.1;
        kwadrat[1] += 0.1;
    }
	
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Execution time: %lf\n", time_spent);
	//Py_RETURN_NONE; //jesli nic nie zwraca
    free(X);
    free(Y);
	return PyFloat_FromDouble(trafiony/wszystkie);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
