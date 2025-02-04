// API基础URL
const API_BASE_URL = '/api';

new Vue({
    el: '#app',
    data: {
        courses: [],
        dialogVisible: false,
        dialogTitle: '添加课程',
        isEdit: false,
        searchForm: {
            Cno: '',
            Cname: '',
            Tno: ''
        },
        form: {
            Cno: '',
            Cname: '',
            Chours: '',
            Credit: 0,
            Tno: '',
            StudentCount: 0
        },
        rules: {
            Cno: [
                { required: true, message: '请输入课程编号', trigger: 'blur' },
                { pattern: /^[A-Za-z]\d{2}$/, message: '课程编号必须是1个字母后跟2位数字', trigger: 'blur' }
            ],
            Cname: [
                { required: true, message: '请输入课程名称', trigger: 'blur' }
            ],
            Chours: [
                { required: true, message: '请输入学时', trigger: 'blur' }
            ],
            Credit: [
                { required: true, message: '请输入学分', trigger: 'blur' },
                { type: 'number', min: 0, message: '学分必须大于等于0', trigger: 'blur' }
            ],
            Tno: [
                { required: true, message: '请输入教师编号', trigger: 'blur' }
            ],
            StudentCount: [
                { type: 'number', min: 0, message: '选课人数必须大于等于0', trigger: 'blur' }
            ]
        }
    },
    created() {
        this.fetchCourses();
    },
    methods: {
        // 获取课程列表
        async fetchCourses(params = {}) {
            try {
                console.log('Fetching courses with params:', params);
                const response = await axios.get(`${API_BASE_URL}/courses`, { params });
                console.log('Response:', response.data);
                
                if (response.data.code === 200) {
                    if (response.data.data && response.data.data.items) {
                        this.courses = response.data.data.items;
                        console.log('Courses loaded:', this.courses);
                    } else {
                        console.error('Invalid data format:', response.data);
                        this.$message.error('数据格式错误');
                    }
                } else {
                    this.$message.error(response.data.message || '获取课程列表失败');
                }
            } catch (error) {
                console.error('Error details:', error);
                this.$message.error(error.response?.data?.message || '网络错误，请稍后重试');
            }
        },

        // 处理搜索
        handleSearch() {
            const params = {};
            if (this.searchForm.Cno) params.Cno = this.searchForm.Cno;
            if (this.searchForm.Cname) params.Cname = this.searchForm.Cname;
            if (this.searchForm.Tno) params.Tno = this.searchForm.Tno;
            this.fetchCourses(params);
        },

        // 重置搜索
        resetSearch() {
            this.searchForm = {
                Cno: '',
                Cname: '',
                Tno: ''
            };
            this.fetchCourses();
        },

        // 显示添加对话框
        showAddDialog() {
            this.dialogTitle = '添加课程';
            this.isEdit = false;
            this.form = {
                Cno: '',
                Cname: '',
                Chours: '',
                Credit: 0,
                Tno: '',
                StudentCount: 0
            };
            this.$nextTick(() => {
                this.$refs.form && this.$refs.form.clearValidate();
            });
            this.dialogVisible = true;
        },

        // 显示编辑对话框
        handleEdit(row) {
            this.dialogTitle = '编辑课程';
            this.isEdit = true;
            this.form = { ...row };
            this.$nextTick(() => {
                this.$refs.form && this.$refs.form.clearValidate();
            });
            this.dialogVisible = true;
        },

        // 删除课程
        handleDelete(row) {
            this.$confirm('确认删除该课程信息吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(async () => {
                try {
                    const response = await axios.delete(`${API_BASE_URL}/courses/${row.Cno}`);
                    if (response.data.code === 200) {
                        this.$message.success('删除成功');
                        this.fetchCourses();
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
                        Credit: parseFloat(this.form.Credit),
                        StudentCount: parseInt(this.form.StudentCount)
                    };

                    if (this.isEdit) {
                        response = await axios.put(`${API_BASE_URL}/courses/${this.form.Cno}`, data);
                    } else {
                        response = await axios.post(`${API_BASE_URL}/courses`, data);
                    }

                    if (response.data.code === 200 || response.data.code === 201) {
                        this.$message.success(this.isEdit ? '更新成功' : '添加成功');
                        this.dialogVisible = false;
                        this.fetchCourses();
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