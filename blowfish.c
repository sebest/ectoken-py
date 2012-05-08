/*
 * gcc -Wl,-soname,_ecblowfish -fPIC -shared -o _ecblowfish.so blowfish.c -lssl
 */

#include <openssl/blowfish.h>
#include <string.h>

#define n2l(c,l)        (l =((unsigned long)(*((c)++)))<<24L, \
                         l|=((unsigned long)(*((c)++)))<<16L, \
                         l|=((unsigned long)(*((c)++)))<< 8L, \
                         l|=((unsigned long)(*((c)++))))

#define l2n(l,c)        (*((c)++)=(unsigned char)(((l)>>24L)&0xff), \
                         *((c)++)=(unsigned char)(((l)>>16L)&0xff), \
                         *((c)++)=(unsigned char)(((l)>> 8L)&0xff), \
                         *((c)++)=(unsigned char)(((l)     )&0xff))

void bfencrypt(unsigned char *keydata, int keydatalen, const unsigned char *in, unsigned char *out, unsigned int inlen);
static void cfb64_encrypt(const unsigned char* in, unsigned char* out, long length, BF_KEY* schedule, unsigned char* ivec, int *num, int encrypt);

/**
 *
 *
 * @param in
 * @param out
 * @param length
 * @param schedule
 * @param ivec
 * @param num
 * @param encrypt
 */

static void cfb64_encrypt(const unsigned char* in, unsigned char* out, long length,
   BF_KEY* schedule,
   unsigned char* ivec,
   int *num,
   int encrypt)
{
  register BF_LONG v0,v1,t;
  register int n= *num;
  register long l=length;
  BF_LONG ti[2];
  unsigned char *iv,c,cc;

  iv=(unsigned char *)ivec;
  while (l--)
  {
    if (n == 0)
    {
      n2l(iv,v0); ti[0]=v0;
      n2l(iv,v1); ti[1]=v1;
      BF_encrypt((BF_LONG*)ti,schedule);
      iv=(unsigned char *)ivec;
      t=ti[0]; l2n(t,iv);
      t=ti[1]; l2n(t,iv);
      iv=(unsigned char *)ivec;
    }
    c= *(in++)^iv[n];
    *(out++)=c;
    iv[n]=c;
    n=(n+1)&0x07;
  }
  v0=v1=ti[0]=ti[1]=t=c=cc=0;
  *num=n;
}

/**
 *
 * @param keydata
 * @param keydatalen
 * @param in
 * @param out
 * @param inlen
 */

void bfencrypt(unsigned char *keydata, int keydatalen, const unsigned char *in, unsigned char *out, unsigned int inlen) {
  BF_KEY key;
  unsigned char ivec[32];
  int num=0;
  /** set up for encryption **/
  BF_set_key(&key, keydatalen, keydata);
  memset(ivec, '\0', 32);
  cfb64_encrypt(in, out, inlen, &key, ivec, &num, BF_ENCRYPT);
}
