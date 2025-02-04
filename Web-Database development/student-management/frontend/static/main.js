// API基础URL
const API_BASE_URL = '/api';

new Vue({
    el: '#app',
    data: {
        students: [],
        dialogVisible: false,
        dialogTitle: '添加学生',
        isEdit: false,
        searchForm: {
            Sno: '',
            Sname: '',
            Dno: ''
        },
        form: {
            Sno: '',
            Sname: '',
            Ssex: '男',
            Sage: 20,
            Dno: '',
            Sclass: '',
            address: ''
        },
        rules: {
            Sno: [
                { required: true, message: '请输入学号', trigger: 'blur' },
                { pattern: /^\d{7}$/, message: '学号必须是7位数字', trigger: 'blur' }
            ],
            Sname: [
                { required: true, message: '请输入姓名', trigger: 'blur' }
            ],
            Ssex: [
                { required: true, message: '请选择性别', trigger: 'change' }
            ],
            Sage: [
                { required: true, message: '请输入年龄', trigger: 'blur' },
                { type: 'number', min: 0, message: '年龄必须大于等于0', trigger: 'blur' }
            ],
            Dno: [
                { required: true, message: '请输入院系', trigger: 'blur' }
            ]
        }
    },
    created() {
        this.fetchStudents();
    },
    methods: {
        // 获取学生列表
        async fetchStudents(params = {}) {
            try {
                console.log('Fetching students with params:', params);
                const response = await axios.get(`${API_BASE_URL}/students`, { params });
                console.log('Response:', response.data);
                
                if (response.data.code === 200) {
                    if (response.data.data && response.data.data.items) {
                        this.students = response.data.data.items;
                        console.log('Students loaded:', this.students);
                    } else {
                        console.error('Invalid data format:', response.data);
                        this.$message.error('数据格式错误');
                    }
                } else {
                    this.$message.error(response.data.message || '获取学生列表失败');
                }
            } catch (error) {
                console.error('Error details:', error);
                this.$message.error('网络错误，请稍后重试');
            }
        },

        // 处理搜索
        handleSearch() {
            const params = {};
            if (this.searchForm.Sno) params.Sno = this.searchForm.Sno;
            if (this.searchForm.Sname) params.Sname = this.searchForm.Sname;
            if (this.searchForm.Dno) params.Dno = this.searchForm.Dno;
            this.fetchStudents(params);
        },

        // 重置搜索
        resetSearch() {
            this.searchForm = {
                Sno: '',
                Sname: '',
                Dno: ''
            };
            this.fetchStudents();
        },

        // 显示添加对话框
        showAddDialog() {
            this.dialogTitle = '添加学生';
            this.isEdit = false;
            this.form = {
                Sno: '',
                Sname: '',
                Ssex: '男',
                Sage: 20,
                Dno: '',
                Sclass: '',
                address: ''
            };
            this.$nextTick(() => {
                this.$refs.form && this.$refs.form.clearValidate();
            });
            this.dialogVisible = true;
        },

        // 显示编辑对话框
        handleEdit(row) {
            this.dialogTitle = '编辑学生';
            this.isEdit = true;
            this.form = { ...row };
            this.$nextTick(() => {
                this.$refs.form && this.$refs.form.clearValidate();
            });
            this.dialogVisible = true;
        },

        // 删除学生
        handleDelete(row) {
            this.$confirm('确认删除该学生信息吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(async () => {
                try {
                    const response = await axios.delete(`${API_BASE_URL}/students/${row.Sno}`);
                    if (response.data.code === 200) {
                        this.$message.success('删除成功');
                        this.fetchStudents();
                    } else {
                        this.$message.error(response.data.message || '删除失败');
                    }
                } catch (error) {
                    this.$message.error('网络错误，请稍后重试');
                    console.error('Error:', error);
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
                    if (this.isEdit) {
                        response = await axios.put(`${API_BASE_URL}/students/${this.form.Sno}`, this.form);
                    } else {
                        response = await axios.post(`${API_BASE_URL}/students`, this.form);
                    }

                    if (response.data.code === 200 || response.data.code === 201) {
                        this.$message.success(this.isEdit ? '更新成功' : '添加成功');
                        this.dialogVisible = false;
                        this.fetchStudents();
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