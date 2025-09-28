#include <efi.h>
#include <efilib.h>
#include <cflags.h>

#include <edk2-flags.h>
#include <edk2-Pcd.h>

#define VA_START(Marker, Parameter)  va_start (Marker, Parameter)
#define VA_ARG(Marker, TYPE)         va_arg (Marker, TYPE)
#define VA_END(Marker)               va_end (Marker)
#define VA_COPY(Dest, Start)         va_copy (Dest, Start)

UINTN EFIAPI AsciiSPrint(CHAR8 *StartOfBuffer, UINTN BufferSize, CONST CHAR8 *FormatString, ...)
{
  va_list  Marker;
  UINTN    NumberOfPrinted;

  VA_START(Marker, FormatString);
  NumberOfPrinted = AsciiVSPrint(StartOfBuffer, BufferSize, FormatString, Marker);
  VA_END(Marker);

  return NumberOfPrinted;
}

UINTN
EFIAPI
AsciiStrLen (
  IN      CONST CHAR8  *String
  )
{
  UINTN  Length;

  ASSERT (String != NULL);

  for (Length = 0; *String != '\0'; String++, Length++) {
    //
    // If PcdMaximumUnicodeStringLength is not zero,
    // length should not more than PcdMaximumUnicodeStringLength
    //
    if (PcdMaximumAsciiStringLength != 0) {
      ASSERT (Length < PcdMaximumAsciiStringLength);
    }
  }

  return Length;
}
