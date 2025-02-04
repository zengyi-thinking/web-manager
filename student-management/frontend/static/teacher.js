// API基础URL
const API_BASE_URL = '/api';

new Vue({
    el: '#app',
    data: {
        teachers: [],
        dialogVisible: false,
        dialogTitle: '添加教师',
        isEdit: false,
        searchForm: {
            Tno: '',
            Tname: '',
            Dno: ''
        },
        form: {
            Tno: '',
            Tname: '',
            Dno: '',
            Salary: 0,
            Tmobile: ''
        },
        rules: {
            Tno: [
                { required: true, message: '请输入教师编号', trigger: 'blur' },
                { pattern: /^\d{3}$/, message: '教师编号必须是3位数字', trigger: 'blur' }
            ],
            Tname: [
                { required: true, message: '请输入教师姓名', trigger: 'blur' }
            ],
            Dno: [
                { required: true, message: '请输入所属院系', trigger: 'blur' }
            ],
            Salary: [
                { required: true, message: '请输入薪资', trigger: 'blur' },
                { type: 'number', min: 0, message: '薪资必须大于等于0', trigger: 'blur' }
            ],
            Tmobile: [
                { pattern: /^1[3-9]\d{9}$/, message: '请输入正确的手机号码', trigger: 'blur' }
            ]
        }
    },
    created() {
        this.fetchTeachers();
    },
    methods: {
        // 获取教师列表
        async fetchTeachers(params = {}) {
            try {
                console.log('Fetching teachers with params:', params);
                const response = await axios.get(`${API_BASE_URL}/teachers`, { params });
                console.log('Response:', response.data);
                
                if (response.data.code === 200) {
                    if (response.data.data && response.data.data.items) {
                        this.teachers = response.data.data.items;
                        console.log('Teachers loaded:', this.teachers);
                    } else {
                        console.error('Invalid data format:', response.data);
                        this.$message.error('数据格式错误');
                    }
                } else {
                    this.$message.error(response.data.message || '获取教师列表失败');
                }
            } catch (error) {
                console.error('Error details:', error);
                this.$message.error(error.response?.data?.message || '网络错误，请稍后重试');
            }
        },

        // 处理搜索
        handleSearch() {
            const params = {};
            if (this.searchForm.Tno) params.Tno = this.searchForm.Tno;
            if (this.searchForm.Tname) params.Tname = this.searchForm.Tname;
            if (this.searchForm.Dno) params.Dno = this.searchForm.Dno;
            this.fetchTeachers(params);
        },

        // 重置搜索
        resetSearch() {
            this.searchForm = {
                Tno: '',
                Tname: '',
                Dno: ''
            };
            this.fetchTeachers();
        },

        // 显示添加对话框
        showAddDialog() {
            this.dialogTitle = '添加教师';
            this.isEdit = false;
            this.form = {
                Tno: '',
                Tname: '',
                Dno: '',
                Salary: 0,
                Tmobile: ''
            };
            this.$nextTick(() => {
                this.$refs.form && this.$refs.form.clearValidate();
            });
            this.dialogVisible = true;
        },

        // 显示编辑对话框
        handleEdit(row) {
            this.dialogTitle = '编辑教师';
            this.isEdit = true;
            this.form = { ...row };
            this.$nextTick(() => {
                this.$refs.form && this.$refs.form.clearValidate();
            });
            this.dialogVisible = true;
        },

        // 删除教师
        handleDelete(row) {
            this.$confirm('确认删除该教师信息吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(async () => {
                try {
                    const response = await axios.delete(`${API_BASE_URL}/teachers/${row.Tno}`);
                    if (response.data.code === 200) {
                        this.$message.success('删除成功');
                        this.fetchTeachers();
                    } else {
                        this.$message.error(response.data.message || '删除失败');
                    }
                } catch (error) {
                    console.error('Error details:', error);
                    this.$message.error(error.response?.data?.message || '网络错误，请稍后重试');
                }
            }).catch(() => {});
        },

        // 提交表单
        submitForm() {
            this.$refs.form.validate(async (valid) => {
                if (!valid) {
                    return;
                }

                try {
                    let response;
                    const data = {
                        ...this.form,
                        Salary: parseFloat(this.form.Salary)
                    };

                    if (this.isEdit) {
                        response = await axios.put(`${API_BASE_URL}/teachers/${this.form.Tno}`, data);
                    } else {
                        response = await axios.post(`${API_BASE_URL}/teachers`, data);
                    }

                    if (response.data.code === 200 || response.data.code === 201) {
                        this.$message.success(this.isEdit ? '更新成功' : '添加成功');
                        this.dialogVisible = false;
                        this.fetchTeachers();
                    } else {
                        this.$message.error(response.data.message || (this.isEdit ? '更新失败' : '添加失败'));
                    }
                } catch (error) {
                    console.error('Error details:', error);
                    this.$message.error(error.response?.data?.message || '网络错误，请稍后重试');
                }
            });
        }
    }
}); 