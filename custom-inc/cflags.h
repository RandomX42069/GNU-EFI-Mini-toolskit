struct __builtin_ms_va_list {
    void* reg_save_area;
    void* overflow_arg_area;
    int gp_offset;
    int fp_offset;
};