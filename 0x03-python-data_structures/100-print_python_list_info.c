#include <stdlib.h>
#include "Python.h"

/**
 * print_python_list_info - funtion prints some info about python list
 * @p : python object
**/

void print_python_list_info(PyObject *p)
{
	const char *type_obj = NULL;
	size_t i = 0, len = 0;
	PylistObject *obj_list = NULL;

	len = PyList_Size(p);
	obj_list = (PyListObject *)p;
	printf("[*] Size of Python List = %ld\n", len);
	printf("[*] Allocated = %li\n", (signed long)(obj_list->allocated));

	for (; i < len; i++)
	{
		type_obj = py_TYPE(obj_list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, py_type);
	}

