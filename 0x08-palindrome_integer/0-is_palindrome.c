/**
 * is_palindrome - checks whether or not a given
 * unsigned integer is a palindrome
 *
 * @n: number to be checked
 *
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
	unsigned long tmp;
	unsigned long rev;

	tmp = n;
	rev = 0;

	while (tmp != 0)
	{
		rev += tmp % 10;
		tmp /= 10;
		if (tmp != 0)
			rev *= 10;
	}
	if (rev == n)
		return (1);
	return (0);
}
