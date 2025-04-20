#include <stdio.h>

// Function to check if a number is prime
int isPrime(int num) {
    // 0 and 1 are not prime numbers
    if (num <= 1) return 0;
    
    // Check divisibility from 2 up to the square root of the number
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0; // Found a divisor, not prime
    }
    
    return 1; // No divisors found, prime number
}

// Function to print all prime numbers up to a given number
void printPrimes(int n) {
    for (int num = 2; num <= n; num++) {
        if (isPrime(num)) {
            printf("%d ", num);
        }
    }
    printf("\n");
}

int main() {
    int n;
    
    // Prompt the user to enter a number
    printf("Enter a number: ");
    scanf("%d", &n);
    
    // Print all prime numbers up to n
    printPrimes(n);
    
    return 0;
}