const { createApp } = Vue;
const searchUrl = FRONT_SEARCH_URL;
const searchUrlAngara = FRONT_SEARCH_URL_ANGARA;
const mainHost = MAIN_HOST;
const mainHostScheme = MAIN_HOST_SCHEME && 'http';

createApp({
  components: {
    EasyDataTable: window['vue3-easy-data-table'],
  },
  delimiters: ['[[', ']]'],
  data() {
    return {
      search: '',
      resCount: 0,
      resCountAngara: 0,
      // Total count of stuff
      totalCount: 0,
      headers: [
        { text: 'НАЗВАНИЕ', value: 'name' },
        { text: 'КАТАЛОГ', value: 'cat' },
        { text: 'БРЕНД', value: 'brand' },
        { text: 'КОЛ-ВО', value: 'stock' },
        { text: 'ЦЕНА', value: 'price', sortable: true },
        { text: 'ПОСТАВЩИК', value: 'supplier_name' },
        { text: 'ДАТА', value: 'updated' },
      ],
      items: [],
      headersAngara: [
        { text: 'НАЗВАНИЕ', value: 'name' },
        { text: 'КАТАЛОГ', value: 'cat' },
        { text: 'БРЕНД', value: 'brand' },
        { text: 'КОЛ-ВО', value: 'stock' },
        { text: 'ЦЕНА', value: 'price', sortable: true },
        { text: 'ПОСТАВЩИК', value: 'supplier_name' },
        { text: 'ДАТА', value: 'updated' },
      ],
      itemsAngara: [],
      showTable: false,
      showTableAngara: false,
    };
  },
  methods: {
    async callCount() {
      this.totalCount = 0;
      const res = await axios.get(
        `${mainHostScheme}://${mainHost}/total-count/`
      );
      this.totalCount = res.data.count;
    },
    async callSearch() {
      this.items = [];
      this.itemsAngara = [];
      let search = '';
      if (this.search.length > 2) {
        search = this.search;
        const res = await axios.get(`${searchUrl}/${search}/`);
        const data = res.data;
        const rows = data.hits.hits;

        const resAngara = await axios.get(`${searchUrlAngara}/${search}/`);
        const dataAngara = resAngara.data;
        const rowsAngara = dataAngara.hits.hits;
        this.resCountAngara = dataAngara.hits.total.value;

        rowsAngara.forEach((item) => {
          const newItem = {};
          newDate = new Date();
          newItem.name = item._source.name;
          newItem.cat = item._source.cat_number;
          newItem.brand = item._source.brand.name.toUpperCase();
          newItem.slug = item._source.slug;
          if (item._source.stocks) {
            newItem.price =
              item._source.stocks.length && item._source.stocks[0].price;
            newItem.stock =
              item._source.stocks.length && item._source.stocks[0].quantity;
          }
          newItem.supplier_name = 'ANGARA';
          newItem.updated = newDate.toLocaleDateString('ru-RU');
          newItem.one_c_id = item._source.one_c_id;

          newItem.car =
            item._source.model && item._source.model[0].name.toUpperCase();
          newItem.img = '';
          if (item._source.images) {
            newItem.img = item._source.images[0].image;
          }
          this.itemsAngara.push({ ...newItem });
        });

        rows.forEach((item) => {
          item._source.price = parseInt(item._source.price);
          date = Date.parse(item._source.updated);
          newDate = new Date(date);
          item._source.updated = newDate.toLocaleDateString('ru-RU');
          item._source.supplier_name =
            item._source.supplier_name &&
            item._source.supplier_name.toUpperCase();
          this.items.push({ ...item._source });
        });
        this.resCount = data.hits.total.value;
        if (this.itemsAngara.length > 0) {
          this.showTableAngara = true;
        }
        if (this.items.length > 0) {
          this.showTable = true;
        }
      }
      if (search.length < 2) {
        this.showTable = false;
        this.showTableAngara = false;
      }
    },
  },
  created() {
    this.callCount();
  },
}).mount('#app');
