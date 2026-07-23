#include <stdio.h>
#include <string.h>
#include <openssl/des.h>

int main()
{
    /* 64-bit DES Key */
    DES_cblock key = {
        0x13,0x34,0x57,0x79,
        0x9B,0xBC,0xDF,0xF1
    };

    DES_key_schedule schedule;
    DES_set_key_unchecked(&key, &schedule);

    /* Ciphertext */
    DES_cblock ciphertext = {
        0x85,0xE8,0x13,0x54,
        0x0F,0x0A,0xB4,0x05
    };

    DES_cblock plaintext;

    /* DES Decryption */
    DES_ecb_encrypt(&ciphertext, &plaintext, &schedule, DES_DECRYPT);

    printf("------------ DES Decryption ------------\n");
    printf("Ciphertext : ");

    for(int i=0;i<8;i++)
        printf("%02X", ciphertext[i]);

    printf("\n");

    printf("Key        : 133457799BBCDFF1\n");

    printf("Plaintext  : ");

    for(int i=0;i<8;i++)
        printf("%c", plaintext[i]);

    printf("\n");

    return 0;
}
