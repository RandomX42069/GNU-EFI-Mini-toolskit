#include <efi.h>
#include <efilib.h>

EFI_STATUS
CreateFileAndWrite(
    EFI_HANDLE ImageHandle,
    CHAR16 *FileName,
    VOID *Buffer,
    UINTN BufferSize
) {
    EFI_STATUS status;
    EFI_LOADED_IMAGE *loaded_image;
    EFI_SIMPLE_FILE_SYSTEM_PROTOCOL *fs;
    EFI_FILE_PROTOCOL *root, *file;

    // Get Loaded Image Protocol
    status = uefi_call_wrapper(BS->HandleProtocol, 3,
        ImageHandle, &LoadedImageProtocol, (void **)&loaded_image);
    if (EFI_ERROR(status)) return status;

    // Get FileSystem protocol from the device we were loaded from
    status = uefi_call_wrapper(BS->HandleProtocol, 3,
        loaded_image->DeviceHandle, &gEfiSimpleFileSystemProtocolGuid, (void **)&fs);
    if (EFI_ERROR(status)) return status;

    // Open root directory
    status = uefi_call_wrapper(fs->OpenVolume, 2, fs, &root);
    if (EFI_ERROR(status)) return status;

    // Open or create the file
    status = uefi_call_wrapper(root->Open, 5, root, &file,
        FileName,
        EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE | EFI_FILE_MODE_CREATE,
        0);
    if (EFI_ERROR(status)) {
        root->Close(root);
        return status;
    }

    // Write buffer to file
    status = uefi_call_wrapper(file->Write, 3, file, &BufferSize, Buffer);

    // Close file + root
    file->Close(file);
    root->Close(root);

    return status;
}

EFI_STATUS
AppendToFile(
    EFI_HANDLE ImageHandle,
    CHAR16 *FileName,
    VOID *Buffer,
    UINTN BufferSize
) {
    EFI_STATUS status;
    EFI_LOADED_IMAGE *loaded_image;
    EFI_SIMPLE_FILE_SYSTEM_PROTOCOL *fs;
    EFI_FILE_PROTOCOL *root, *file;

    // Get Loaded Image Protocol
    status = uefi_call_wrapper(BS->HandleProtocol, 3,
        ImageHandle,
        &gEfiLoadedImageProtocolGuid,
        (void **)&loaded_image);
    if (EFI_ERROR(status)) return status;

    // Get FS protocol
    status = uefi_call_wrapper(BS->HandleProtocol, 3,
        loaded_image->DeviceHandle,
        &gEfiSimpleFileSystemProtocolGuid,
        (void **)&fs);
    if (EFI_ERROR(status)) return status;

    // Open root dir
    status = uefi_call_wrapper(fs->OpenVolume, 2, fs, &root);
    if (EFI_ERROR(status)) return status;

    // Open or create file
    status = uefi_call_wrapper(root->Open, 5, root, &file,
        FileName,
        EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE | EFI_FILE_MODE_CREATE,
        0);
    if (EFI_ERROR(status)) {
        root->Close(root);
        return status;
    }

    // Move file cursor to end
    status = uefi_call_wrapper(file->SetPosition, 2, file, (UINT64)-1);
    if (EFI_ERROR(status)) {
        file->Close(file);
        root->Close(root);
        return status;
    }

    // Write buffer at the end
    status = uefi_call_wrapper(file->Write, 3, file, &BufferSize, Buffer);

    // Cleanup
    file->Close(file);
    root->Close(root);

    return status;
}
