#include <stdio.h>
#include <string.h>
#include <openssl/des.h>

int main()
{
    DES_cblock key = "A1B2C3D4";
    DES_key_schedule schedule;

    char plaintext[9] = "COMPUTER";
    DES_cblock input;
    DES_cblock output;

    memcpy(input, plaintext, 8);

    DES_set_key_unchecked(&key, &schedule);

    DES_ecb_encrypt(&input, &output, &schedule, DES_ENCRYPT);

    printf("Plaintext : %s\n", plaintext);
    printf("Key       : %s\n", key);

    printf("Ciphertext (Hex): ");

    for(int i=0;i<8;i++)
        printf("%02X", output[i]);

    printf("\n");

    return 0;
}
