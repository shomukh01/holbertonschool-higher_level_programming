#ifndef VARIADIC_FUNCTIONS_H
#define VARIADIC_FUNCTIONS_H

#include <stdarg.h>

/**
 * sum_them_all - returns the sum of all its parameters
 * @n: number of arguments
 *
 * Return: sum
 */
int sum_them_all(const unsigned int n, ...);

/**
 * print_numbers - prints numbers
 * @separator: string to separate numbers
 * @n: number of arguments
 */
void print_numbers(const char *separator, const unsigned int n, ...);

/**
 * print_strings - prints strings
 * @separator: string to separate strings
 * @n: number of arguments
 */
void print_strings(const char *separator, const unsigned int n, ...);

/**
 * print_all - prints anything
 * @format: list of types
 */
void print_all(const char * const format, ...);

#endif
