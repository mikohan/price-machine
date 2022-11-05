const { createApp } = Vue;
const searchUrl = FRONT_SEARCH_URL;

createApp({
  components: {
    EasyDataTable: window['vue3-easy-data-table'],
  },
  delimiters: ['[[', ']]'],
  data() {
    return {
      search: '',
      resCount: null,
      headers: [
        { text: 'НАЗВАНИЕ', value: 'name' },
        { text: 'КАТАЛОГ', value: 'cat' },
        { text: 'КОЛ-ВО', value: 'stock' },
        { text: 'ЦЕНА', value: 'price', sortable: true },
        { text: 'ПОСТАВЩИК', value: 'supplier_name' },
        { text: 'ДАТА', value: 'updated' },
      ],
      items: [],
    };
  },
  methods: {
    async callSearch() {
      console.log(this.search);
      const res = await axios.get(searchUrl);
      const data = res.data;
      const rows = data.hits.hits;
      rows.forEach((item) => {
        item._source.price = parseInt(item._source.price);
        date = Date.parse(item._source.updated);
        newDate = new Date(date);
        item._source.updated = newDate.toLocaleDateString('ru-RU');
        this.items.push({ ...item._source });
      });
      this.resCount = data.hits.total.value;
    },
  },
  created() {
    this.callSearch();
  },
}).mount('#app');
