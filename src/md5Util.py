import hashlib

m = hashlib.md5()
a = 'webpackJsonp([1],Array(45).concat([function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var a=i(15),r=n(a),s=i(130),o=n(s);r.default.use(o.default);var l={fastprint:i(120)},u=new o.default({linkActiveClass:"cur",routes:[{path:"/",name:"index",meta:{title:"网上冲印"},component:l.fastprint},{path:"/fastprint",name:"fastprint",meta:{title:"网上冲印"},component:l.fastprint}]});u.beforeEach(function(t,e,i){t.meta.title?document.title=t.meta.title:document.title="网上冲印",i()}),e.default=u},,function(t,e,i){i(107);var n=i(1)(i(50),i(127),null,null);t.exports=n.exports},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"swiper-slide",data:function(){return{slideClass:"swiper-slide"}},ready:function(){this.update()},mounted:function(){this.update(),this.$parent.options.slideClass&&(this.slideClass=this.$parent.options.slideClass)},updated:function(){this.update()},attached:function(){this.update()},methods:{update:function(){this.$parent&&this.$parent.swiper&&this.$parent.swiper.update&&(this.$parent.swiper.update(!0),this.$parent.options.loop&&this.$parent.swiper.reLoop())}}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n="undefined"!=typeof window;n&&(window.Swiper=i(43)),e.default={name:"swiper",props:{options:{type:Object,default:function(){return{autoplay:3500}}},notNextTick:{type:Boolean,default:function(){return!1}}},data:function(){return{defaultSwiperClasses:{wrapperClass:"swiper-wrapper"}}},ready:function(){!this.swiper&&n&&(this.swiper=new Swiper(this.$el,this.options))},mounted:function(){var t=this,e=function(){if(!t.swiper&&n){delete t.options.notNextTick;var e=!1;for(var i in t.defaultSwiperClasses)t.defaultSwiperClasses.hasOwnProperty(i)&&t.options[i]&&(e=!0,t.defaultSwiperClasses[i]=t.options[i]);var a=function(){t.swiper=new Swiper(t.$el,t.options)};e?t.$nextTick(a):a()}}(this.options.notNextTick||this.notNextTick)?e():this.$nextTick(e)},updated:function(){this.swiper&&this.swiper.update()},beforeDestroy:function(){this.swiper&&(this.swiper.destroy(),delete this.swiper)}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"app",components:{},created:function(){}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i(112);e.default={data:function(){return{swiperOption:{initialSlide:0,loop:!1,effect:"slide",pagination:".swiper-pagination",onSlideChangeEnd:function(t){}}}},created:function(){},methods:{isInMp:function(){return!(!window.__wxjs_environment||"miniprogram"!==window.__wxjs_environment)}},props:{},components:{swiper:n.swiper,swiperSlide:n.swiperSlide}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},props:{dataList:Array,clk:Function},created:function(){},methods:{},components:{}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},props:{imgsrc:String},created:function(){},methods:{},components:{}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},created:function(){},props:{sinfo:String,minfo:String,binfo:String,price:String},methods:{},components:{}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},props:{dataList:Array,title:String,subTitle:String,clk:Function},computed:{},beforeUpdate:function(){}}},function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var a=i(59),r=n(a),s=i(60),o=n(s),l=i(116),u=n(l),c=i(117),f=n(c),d=i(118),p=n(d),v=i(119),m=n(v),h=i(115),g=n(h),_=i(58),b=n(_);e.default={data:function(){return{navList:[],demosrc:"//img11.360buyimg.com/uba/jfs/t9106/352/1858495565/55229/c92175ee/59bf8a08N0da3c14f.png",currInfo:{nav:"normal",size:"5寸",sizeFlag:0,material:"绒面",materialFlag:0,brand:"富士",brandFlag:0,price:"0.1",sku:2852406},printBagNum:0,sizeList:[],sizeListTitle:"选择尺寸",brandList:[],brandListTitle:"选择品牌",brandListSubTitle:"富士：色彩逼真",materialList:[],materialListTitle:"选择相纸",materialListSubTitle:"绒面：不易留手印，推荐人像照",totalData:{},skusMap:{},isiPhoneX:!1}},mounted:function(){},created:function(){var t=this;if(b.default.getInitFastPrintData().then(function(e){t.totalData=JSON.parse(e.bodyText),t.sizeList=t.totalData.normal.sizeList,t.brandList=t.totalData.normal.brandList,t.materialList=t.totalData.normal.materialList,t.navList=t.totalData.nav,t.getPrice();var i=new o.default,n=!0,a=!1,s=void 0;try{for(var l,u=(0,r.default)(t.totalData.skuList);!(n=(l=u.next()).done);n=!0){var c=l.value;i.set(c.k,c.v)}}catch(t){a=!0,s=t}finally{try{!n&&u.return&&u.return()}finally{if(a)throw s}}t.skusMap=i}),window.__wxjs_environment&&"miniprogram"===window.__wxjs_environment&&-1==window.location.href.indexOf("isLogin=true")){var e=function(t){t.errcode};p_logout.logout(e,"jd.com",269)}b.default.getPrintBagNum().then(function(e){t.printBagNum=JSON.parse(e.bodyText).result.num})},methods:{handleClkNav:function(t){var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.navList);!(e=(a=s.next()).done);e=!0){var o=a.value;o.c=1,o.v===t.target.title&&(o.c=0)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.resetTotalData(t.target.title),this.currInfo.nav=t.target.title,this.getPrice()},handleClkSize:function(t){if("normal"===this.currInfo.nav){if(1===this.currInfo.brandFlag&&3===t.target.value)return;3===t.target.value||1===this.currInfo.materialFlag?this.brandList[1].c=2:0==this.brandList[1].c?this.brandList[1].c=0:this.brandList[1].c=1}var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.sizeList);!(e=(a=s.next()).done);e=!0){var o=a.value;2!==o.c&&(o.c=1),o.v===t.target.value&&(o.c=0,this.demosrc=o.i,this.currInfo.size=o.k)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.currInfo.sizeFlag=t.target.value,this.setCurrSku(this.currInfo.nav),this.getPrice()},handleClkBrand:function(t){if("normal"===this.currInfo.nav){if(1===this.currInfo.materialFlag&&1===t.target.value||3===this.currInfo.sizeFlag&&1===t.target.value)return;1===t.target.value?(this.sizeList[3].c=2,this.materialList[1].c=2):(0==this.sizeList[3].c?this.sizeList[3].c=0:this.sizeList[3].c=1,0==this.materialList[1].c?this.materialList[1].c=0:this.materialList[1].c=1)}var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.brandList);!(e=(a=s.next()).done);e=!0){var o=a.value;2!==o.c&&(o.c=1),o.v===t.target.value&&(o.c=0,this.currInfo.brand=o.k,this.brandListSubTitle=o.k+"："+o.d)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.currInfo.brandFlag=t.target.value,this.setCurrSku(this.currInfo.nav),this.getPrice()},handleClkMaterial:function(t){if("normal"===this.currInfo.nav){if(1===this.currInfo.brandFlag&&1===t.target.value)return;1===t.target.value?this.brandList[1].c=2:0==this.brandList[1].c?this.brandList[1].c=0:this.brandList[1].c=1}var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.materialList);!(e=(a=s.next()).done);e=!0){var o=a.value;2!==o.c&&(o.c=1),o.v===t.target.value&&(o.c=0,this.currInfo.material=o.k,this.materialListSubTitle=o.k+"："+o.d)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.currInfo.materialFlag=t.target.value,this.setCurrSku(this.currInfo.nav),this.getPrice()},resetTotalData:function(t){var e=this;b.default.getInitFastPrintData().then(function(i){e.totalData=JSON.parse(i.bodyText),e.sizeList=e.totalData[t].sizeList,e.brandList=e.totalData[t].brandList,e.materialList=e.totalData[t].materialList,e.currInfo.size=e.totalData[t].sizeList[0].k,e.currInfo.sizeFlag=e.totalData[t].sizeList[0].v,e.currInfo.brand=e.totalData[t].brandList[0].k,e.currInfo.brandFlag=e.totalData[t].brandList[0].v,e.brandListSubTitle=e.totalData[t].brandList[0].k+"："+e.totalData[t].brandList[0].d,e.materialListSubTitle=e.totalData[t].materialList[0].k+"："+e.totalData[t].materialList[0].d,e.currInfo.material=e.totalData[t].materialList[0].k,e.currInfo.materialFlag=e.totalData[t].materialList[0].v,e.demosrc=e.totalData[t].sizeList[0].i,e.setCurrSku(t)})},getPrice:function(){var t=this;setTimeout(function(){b.default.getSkuPrice(t.currInfo.sku).then(function(e){t.currInfo.price=JSON.parse(e.bodyText).result.printingProductVo.price.toString()})},300)},setCurrSku:function(t){this.currInfo.sku=this.skusMap.get(t+"_s"+this.currInfo.sizeFlag+"b"+this.currInfo.brandFlag+"m"+this.currInfo.materialFlag)},goPrintBag:function(){this.checkLogin()&&(location.href="//printmini.m.jd.com/printingBag/toPrintingBagPage")},goPrint:function(){this.checkLogin()&&(location.href="//printmini.m.jd.com/printingApi/init?jdshwkoff=1&skuId="+this.currInfo.sku)},checkLogin:function(){return!window.__wxjs_environment||"miniprogram"!==window.__wxjs_environment||-1!=window.location.href.indexOf("isLogin=true")||(window.wx.miniProgram.navigateTo({url:"/pages/login/login?returnPage="+encodeURIComponent("/pages/index/index")+"&fromPageType=switchTab"}),!1)}},beforeUpdate:function(){},components:{fpnav:u.default,fpdemo:f.default,fpinfo:p.default,fpselection:m.default,fpad:g.default}}},function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}var a=i(15),r=n(a),s=i(47),o=n(s),l=i(45),u=n(l),c=i(25),f=n(c),d=i(46),p=n(d);r.default.config.devtools=!0,r.default.use(f.default),r.default.use(p.default),r.default.http.interceptors.push(function(t,e){e(function(t){203===t.body.code&&(location.href=t.body.data.loginUrl+"&returnurl="+encodeURIComponent(location.href))})}),new r.default({el:"#app",router:u.default,template:"<App/>",components:{App:o.default}})},function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var a=i(62),r=n(a),s=i(63),o=n(s),l=i(15),u=n(l),c=i(25),f=n(c);u.default.use(f.default);var d=function(){function t(){(0,r.default)(this,t)}return(0,o.default)(t,null,[{key:"getInitFastPrintData",value:function(){return u.default.http.jsonp("//misc.360buyimg.com/m/online_print_fastprint/1.0.0/photoData.json",{jsonp:"callback",jsonpCallback:"dataHandler"})}},{key:"getSkuPrice",value:function(t){return u.default.http.jsonp("//printmini.m.jd.com/printingApi/getPrintingSkuPrice?defaultSkuId="+t,{jsonp:"callback"})}},{key:"getPrintBagNum",value:function(){return u.default.http.jsonp("//printmini.m.jd.com/printingBagApi/getPrintingBagCount",{jsonp:"callback"})}}]),t}();e.default=d},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},,,,,function(t,e,i){var n=i(1)(i(48),i(129),null,null);t.exports=n.exports},function(t,e,i){var n=i(1)(i(49),i(123),null,null);t.exports=n.exports},function(t,e,i){i(103);var n=i(1)(i(51),i(122),null,null);t.exports=n.exports},function(t,e,i){i(106);var n=i(1)(i(52),i(126),"data-v-547e9dae",null);t.exports=n.exports},function(t,e,i){i(104);var n=i(1)(i(53),i(124),"data-v-3de6dc60",null);t.exports=n.exports},function(t,e,i){i(102);var n=i(1)(i(54),i(121),"data-v-1572e5ab",null);t.exports=n.exports},function(t,e,i){i(105);var n=i(1)(i(55),i(125),"data-v-45316757",null);t.exports=n.exports},function(t,e,i){i(108);var n=i(1)(i(56),i(128),"data-v-7b6716fb",null);t.exports=n.exports},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"info-continer"},[i("span",{staticClass:"info-arrow"}),t._v(" "),i("div",{staticClass:"info-cont"},[i("span",[t._v("已选："+t._s(t.sinfo?t.sinfo+"，":"")+" "+t._s(t.binfo?t.binfo+"，":t.binfo)+" "+t._s(t.minfo?t.minfo+"，":t.minfo))]),t._v(" "),i("span",{staticClass:"fontred"},[t._v(t._s(Number(t.price).toFixed(2))+"元/张")])])])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"adcontiner"},[t.isInMp()?t._e():i("swiper",{attrs:{options:t.swiperOption}},[i("swiper-slide",{staticClass:"ad-item"},[i("a",{attrs:{href:"//pro.m.jd.com/mall/active/nWBmH5F11RFNQ4uprCwC5pCtbKn/index.html"}},[i("img",{attrs:{src:"//img13.360buyimg.com/cms/jfs/t8530/39/1949178066/195729/81a6474b/59c2275bNccc64340.jpg!q50",alt:""}})])]),t._v(" "),i("div",{staticClass:"swiper-pagination",attrs:{slot:"pagination"},slot:"pagination"})],1)],1)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"swiper-container"},[t._t("parallax-bg"),t._v(" "),i("div",{class:t.defaultSwiperClasses.wrapperClass},[t._t("default")],2),t._v(" "),t._t("pagination"),t._v(" "),t._t("button-prev"),t._v(" "),t._t("button-next"),t._v(" "),t._t("scrollbar")],2)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"fp-demo-main"},[i("img",{attrs:{src:t.imgsrc,alt:""}})])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return t.dataList.length>0?i("div",{staticClass:"selection-continer"},[i("h3",[t._v(t._s(t.title)),i("span",[t._v(t._s(t.subTitle))])]),t._v(" "),i("div",{staticClass:"selection-items"},[i("ul",t._l(t.dataList,function(e,n){return i("li",{key:n,class:{curr:"0"==e.c,disable:"2"==e.c},attrs:{value:e.v},on:{click:t.clk}},[t._v(t._s(e.k))])}))])]):t._e()},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("header",[i("ul",t._l(t.dataList,function(e,n){return i("li",{key:n,class:{curr:0===e.c},attrs:{value:e.v,title:e.v},on:{click:t.clk}},[t._v(t._s(e.type))])}))])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"container",attrs:{id:"app"}},[i("router-view")],1)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("fpnav",{attrs:{dataList:t.navList,clk:t.handleClkNav}}),t._v(" "),i("fpdemo",{attrs:{imgsrc:t.demosrc}}),t._v(" "),i("fpinfo",{attrs:{sinfo:t.currInfo.size,minfo:t.currInfo.material,binfo:t.currInfo.brand,price:t.currInfo.price}}),t._v(" "),i("fpselection",{attrs:{title:t.sizeListTitle,dataList:t.sizeList,clk:t.handleClkSize}}),t._v(" "),i("fpselection",{attrs:{title:t.brandListTitle,subTitle:t.brandListSubTitle,dataList:t.brandList,clk:t.handleClkBrand}}),t._v(" "),i("fpselection",{attrs:{title:t.materialListTitle,subTitle:t.materialListSubTitle,dataList:t.materialList,clk:t.handleClkMaterial}}),t._v(" "),i("fpad"),t._v(" "),i("footer",[i("span",{staticClass:"printbag",on:{click:t.goPrintBag}},[i("i",[i("em",[t._v(t._s(t.printBagNum))])]),t._v(" "),i("b",[t._v("冲印袋")])]),t._v(" "),i("span",{staticClass:"submit",on:{click:t.goPrint}},[t._v("立即冲印")])])],1)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement;return(t._self._c||e)("div",{class:t.slideClass},[t._t("default")],2)},staticRenderFns:[]}},,,function(t,e){}]),[57]);'
b = 'webpackJsonp([1],Array(45).concat([function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var a=i(15),r=n(a),s=i(130),o=n(s);r.default.use(o.default);var l={fastprint:i(120)},u=new o.default({linkActiveClass:"cur",routes:[{path:"/",name:"index",meta:{title:"网上冲印"},component:l.fastprint},{path:"/fastprint",name:"fastprint",meta:{title:"网上冲印"},component:l.fastprint}]});u.beforeEach(function(t,e,i){t.meta.title?document.title=t.meta.title:document.title="网上冲印",i()}),e.default=u},,function(t,e,i){i(107);var n=i(1)(i(50),i(127),null,null);t.exports=n.exports},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"swiper-slide",data:function(){return{slideClass:"swiper-slide"}},ready:function(){this.update()},mounted:function(){this.update(),this.$parent.options.slideClass&&(this.slideClass=this.$parent.options.slideClass)},updated:function(){this.update()},attached:function(){this.update()},methods:{update:function(){this.$parent&&this.$parent.swiper&&this.$parent.swiper.update&&(this.$parent.swiper.update(!0),this.$parent.options.loop&&this.$parent.swiper.reLoop())}}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n="undefined"!=typeof window;n&&(window.Swiper=i(43)),e.default={name:"swiper",props:{options:{type:Object,default:function(){return{autoplay:3500}}},notNextTick:{type:Boolean,default:function(){return!1}}},data:function(){return{defaultSwiperClasses:{wrapperClass:"swiper-wrapper"}}},ready:function(){!this.swiper&&n&&(this.swiper=new Swiper(this.$el,this.options))},mounted:function(){var t=this,e=function(){if(!t.swiper&&n){delete t.options.notNextTick;var e=!1;for(var i in t.defaultSwiperClasses)t.defaultSwiperClasses.hasOwnProperty(i)&&t.options[i]&&(e=!0,t.defaultSwiperClasses[i]=t.options[i]);var a=function(){t.swiper=new Swiper(t.$el,t.options)};e?t.$nextTick(a):a()}}(this.options.notNextTick||this.notNextTick)?e():this.$nextTick(e)},updated:function(){this.swiper&&this.swiper.update()},beforeDestroy:function(){this.swiper&&(this.swiper.destroy(),delete this.swiper)}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"app",components:{},created:function(){}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i(112);e.default={data:function(){return{swiperOption:{initialSlide:0,loop:!1,effect:"slide",pagination:".swiper-pagination",onSlideChangeEnd:function(t){}}}},created:function(){},methods:{},props:{},components:{swiper:n.swiper,swiperSlide:n.swiperSlide}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},props:{dataList:Array,clk:Function},created:function(){},methods:{},components:{}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},props:{imgsrc:String},created:function(){},methods:{},components:{}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},created:function(){},props:{sinfo:String,minfo:String,binfo:String,price:String},methods:{},components:{}}},function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={data:function(){return{}},props:{dataList:Array,title:String,subTitle:String,clk:Function},computed:{},beforeUpdate:function(){}}},function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var a=i(59),r=n(a),s=i(60),o=n(s),l=i(116),u=n(l),c=i(117),f=n(c),d=i(118),p=n(d),v=i(119),m=n(v),h=i(115),g=n(h),_=i(58),b=n(_);e.default={data:function(){return{navList:[],demosrc:"//img11.360buyimg.com/uba/jfs/t9106/352/1858495565/55229/c92175ee/59bf8a08N0da3c14f.png",currInfo:{nav:"normal",size:"5寸",sizeFlag:0,material:"绒面",materialFlag:0,brand:"富士",brandFlag:0,price:"0.1",sku:2852406},printBagNum:0,sizeList:[],sizeListTitle:"选择尺寸",brandList:[],brandListTitle:"选择品牌",brandListSubTitle:"富士：色彩逼真",materialList:[],materialListTitle:"选择相纸",materialListSubTitle:"绒面：不易留手印，推荐人像照",totalData:{},skusMap:{},isiPhoneX:!1}},mounted:function(){},created:function(){var t=this;if(b.default.getInitFastPrintData().then(function(e){t.totalData=JSON.parse(e.bodyText),t.sizeList=t.totalData.normal.sizeList,t.brandList=t.totalData.normal.brandList,t.materialList=t.totalData.normal.materialList,t.navList=t.totalData.nav,t.getPrice();var i=new o.default,n=!0,a=!1,s=void 0;try{for(var l,u=(0,r.default)(t.totalData.skuList);!(n=(l=u.next()).done);n=!0){var c=l.value;i.set(c.k,c.v)}}catch(t){a=!0,s=t}finally{try{!n&&u.return&&u.return()}finally{if(a)throw s}}t.skusMap=i}),window.__wxjs_environment&&"miniprogram"===window.__wxjs_environment&&-1==window.location.href.indexOf("isLogin=true")){var e=function(t){t.errcode};p_logout.logout(e,"jd.com",269)}b.default.getPrintBagNum().then(function(e){t.printBagNum=JSON.parse(e.bodyText).result.num})},methods:{handleClkNav:function(t){var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.navList);!(e=(a=s.next()).done);e=!0){var o=a.value;o.c=1,o.v===t.target.title&&(o.c=0)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.resetTotalData(t.target.title),this.currInfo.nav=t.target.title,this.getPrice()},handleClkSize:function(t){if("normal"===this.currInfo.nav){if(1===this.currInfo.brandFlag&&3===t.target.value)return;3===t.target.value||1===this.currInfo.materialFlag?this.brandList[1].c=2:0==this.brandList[1].c?this.brandList[1].c=0:this.brandList[1].c=1}var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.sizeList);!(e=(a=s.next()).done);e=!0){var o=a.value;2!==o.c&&(o.c=1),o.v===t.target.value&&(o.c=0,this.demosrc=o.i,this.currInfo.size=o.k)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.currInfo.sizeFlag=t.target.value,this.setCurrSku(this.currInfo.nav),this.getPrice()},handleClkBrand:function(t){if("normal"===this.currInfo.nav){if(1===this.currInfo.materialFlag&&1===t.target.value||3===this.currInfo.sizeFlag&&1===t.target.value)return;1===t.target.value?(this.sizeList[3].c=2,this.materialList[1].c=2):(0==this.sizeList[3].c?this.sizeList[3].c=0:this.sizeList[3].c=1,0==this.materialList[1].c?this.materialList[1].c=0:this.materialList[1].c=1)}var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.brandList);!(e=(a=s.next()).done);e=!0){var o=a.value;2!==o.c&&(o.c=1),o.v===t.target.value&&(o.c=0,this.currInfo.brand=o.k,this.brandListSubTitle=o.k+"："+o.d)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.currInfo.brandFlag=t.target.value,this.setCurrSku(this.currInfo.nav),this.getPrice()},handleClkMaterial:function(t){if("normal"===this.currInfo.nav){if(1===this.currInfo.brandFlag&&1===t.target.value)return;1===t.target.value?this.brandList[1].c=2:0==this.brandList[1].c?this.brandList[1].c=0:this.brandList[1].c=1}var e=!0,i=!1,n=void 0;try{for(var a,s=(0,r.default)(this.materialList);!(e=(a=s.next()).done);e=!0){var o=a.value;2!==o.c&&(o.c=1),o.v===t.target.value&&(o.c=0,this.currInfo.material=o.k,this.materialListSubTitle=o.k+"："+o.d)}}catch(t){i=!0,n=t}finally{try{!e&&s.return&&s.return()}finally{if(i)throw n}}this.currInfo.materialFlag=t.target.value,this.setCurrSku(this.currInfo.nav),this.getPrice()},resetTotalData:function(t){var e=this;b.default.getInitFastPrintData().then(function(i){e.totalData=JSON.parse(i.bodyText),e.sizeList=e.totalData[t].sizeList,e.brandList=e.totalData[t].brandList,e.materialList=e.totalData[t].materialList,e.currInfo.size=e.totalData[t].sizeList[0].k,e.currInfo.sizeFlag=e.totalData[t].sizeList[0].v,e.currInfo.brand=e.totalData[t].brandList[0].k,e.currInfo.brandFlag=e.totalData[t].brandList[0].v,e.brandListSubTitle=e.totalData[t].brandList[0].k+"："+e.totalData[t].brandList[0].d,e.materialListSubTitle=e.totalData[t].materialList[0].k+"："+e.totalData[t].materialList[0].d,e.currInfo.material=e.totalData[t].materialList[0].k,e.currInfo.materialFlag=e.totalData[t].materialList[0].v,e.demosrc=e.totalData[t].sizeList[0].i,e.setCurrSku(t)})},getPrice:function(){var t=this;setTimeout(function(){b.default.getSkuPrice(t.currInfo.sku).then(function(e){t.currInfo.price=JSON.parse(e.bodyText).result.printingProductVo.price.toString()})},300)},setCurrSku:function(t){this.currInfo.sku=this.skusMap.get(t+"_s"+this.currInfo.sizeFlag+"b"+this.currInfo.brandFlag+"m"+this.currInfo.materialFlag)},goPrintBag:function(){this.checkLogin()&&(location.href="//printmini.m.jd.com/printingBag/toPrintingBagPage")},goPrint:function(){this.checkLogin()&&(location.href="//printmini.m.jd.com/printingApi/init?jdshwkoff=1&skuId="+this.currInfo.sku)},checkLogin:function(){return!window.__wxjs_environment||"miniprogram"!==window.__wxjs_environment||-1!=window.location.href.indexOf("isLogin=true")||(window.wx.miniProgram.navigateTo({url:"/pages/login/login?returnPage="+encodeURIComponent("/pages/index/index")+"&fromPageType=switchTab"}),!1)},isInMp:function(){return!(!window.__wxjs_environment||"miniprogram"!==window.__wxjs_environment)}},beforeUpdate:function(){},components:{fpnav:u.default,fpdemo:f.default,fpinfo:p.default,fpselection:m.default,fpad:g.default}}},function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}var a=i(15),r=n(a),s=i(47),o=n(s),l=i(45),u=n(l),c=i(25),f=n(c),d=i(46),p=n(d);r.default.config.devtools=!0,r.default.use(f.default),r.default.use(p.default),r.default.http.interceptors.push(function(t,e){e(function(t){203===t.body.code&&(location.href=t.body.data.loginUrl+"&returnurl="+encodeURIComponent(location.href))})}),new r.default({el:"#app",router:u.default,template:"<App/>",components:{App:o.default}})},function(t,e,i){"use strict";function n(t){return t&&t.__esModule?t:{default:t}}Object.defineProperty(e,"__esModule",{value:!0});var a=i(62),r=n(a),s=i(63),o=n(s),l=i(15),u=n(l),c=i(25),f=n(c);u.default.use(f.default);var d=function(){function t(){(0,r.default)(this,t)}return(0,o.default)(t,null,[{key:"getInitFastPrintData",value:function(){return u.default.http.jsonp("//misc.360buyimg.com/m/online_print_fastprint/1.0.0/photoData.json",{jsonp:"callback",jsonpCallback:"dataHandler"})}},{key:"getSkuPrice",value:function(t){return u.default.http.jsonp("//printmini.m.jd.com/printingApi/getPrintingSkuPrice?defaultSkuId="+t,{jsonp:"callback"})}},{key:"getPrintBagNum",value:function(){return u.default.http.jsonp("//printmini.m.jd.com/printingBagApi/getPrintingBagCount",{jsonp:"callback"})}}]),t}();e.default=d},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},,,,,function(t,e,i){var n=i(1)(i(48),i(129),null,null);t.exports=n.exports},function(t,e,i){var n=i(1)(i(49),i(123),null,null);t.exports=n.exports},function(t,e,i){i(103);var n=i(1)(i(51),i(122),null,null);t.exports=n.exports},function(t,e,i){i(106);var n=i(1)(i(52),i(126),"data-v-547e9dae",null);t.exports=n.exports},function(t,e,i){i(104);var n=i(1)(i(53),i(124),"data-v-3de6dc60",null);t.exports=n.exports},function(t,e,i){i(102);var n=i(1)(i(54),i(121),"data-v-1572e5ab",null);t.exports=n.exports},function(t,e,i){i(105);var n=i(1)(i(55),i(125),"data-v-45316757",null);t.exports=n.exports},function(t,e,i){i(108);var n=i(1)(i(56),i(128),"data-v-7b6716fb",null);t.exports=n.exports},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"info-continer"},[i("span",{staticClass:"info-arrow"}),t._v(" "),i("div",{staticClass:"info-cont"},[i("span",[t._v("已选："+t._s(t.sinfo?t.sinfo+"，":"")+" "+t._s(t.binfo?t.binfo+"，":t.binfo)+" "+t._s(t.minfo?t.minfo+"，":t.minfo))]),t._v(" "),i("span",{staticClass:"fontred"},[t._v(t._s(Number(t.price).toFixed(2))+"元/张")])])])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"adcontiner"},[i("swiper",{attrs:{options:t.swiperOption}},[i("swiper-slide",{staticClass:"ad-item"},[i("a",{attrs:{href:"//pro.m.jd.com/mall/active/nWBmH5F11RFNQ4uprCwC5pCtbKn/index.html"}},[i("img",{attrs:{src:"//img13.360buyimg.com/cms/jfs/t8530/39/1949178066/195729/81a6474b/59c2275bNccc64340.jpg!q50",alt:""}})])]),t._v(" "),i("div",{staticClass:"swiper-pagination",attrs:{slot:"pagination"},slot:"pagination"})],1)],1)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"swiper-container"},[t._t("parallax-bg"),t._v(" "),i("div",{class:t.defaultSwiperClasses.wrapperClass},[t._t("default")],2),t._v(" "),t._t("pagination"),t._v(" "),t._t("button-prev"),t._v(" "),t._t("button-next"),t._v(" "),t._t("scrollbar")],2)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"fp-demo-main"},[i("img",{attrs:{src:t.imgsrc,alt:""}})])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return t.dataList.length>0?i("div",{staticClass:"selection-continer"},[i("h3",[t._v(t._s(t.title)),i("span",[t._v(t._s(t.subTitle))])]),t._v(" "),i("div",{staticClass:"selection-items"},[i("ul",t._l(t.dataList,function(e,n){return i("li",{key:n,class:{curr:"0"==e.c,disable:"2"==e.c},attrs:{value:e.v},on:{click:t.clk}},[t._v(t._s(e.k))])}))])]):t._e()},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("header",[i("ul",t._l(t.dataList,function(e,n){return i("li",{key:n,class:{curr:0===e.c},attrs:{value:e.v,title:e.v},on:{click:t.clk}},[t._v(t._s(e.type))])}))])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"container",attrs:{id:"app"}},[i("router-view")],1)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("fpnav",{attrs:{dataList:t.navList,clk:t.handleClkNav}}),t._v(" "),i("fpdemo",{attrs:{imgsrc:t.demosrc}}),t._v(" "),i("fpinfo",{attrs:{sinfo:t.currInfo.size,minfo:t.currInfo.material,binfo:t.currInfo.brand,price:t.currInfo.price}}),t._v(" "),i("fpselection",{attrs:{title:t.sizeListTitle,dataList:t.sizeList,clk:t.handleClkSize}}),t._v(" "),i("fpselection",{attrs:{title:t.brandListTitle,subTitle:t.brandListSubTitle,dataList:t.brandList,clk:t.handleClkBrand}}),t._v(" "),i("fpselection",{attrs:{title:t.materialListTitle,subTitle:t.materialListSubTitle,dataList:t.materialList,clk:t.handleClkMaterial}}),t._v(" "),t.isInMp()?t._e():i("fpad"),t._v(" "),i("footer",[i("span",{staticClass:"printbag",on:{click:t.goPrintBag}},[i("i",[i("em",[t._v(t._s(t.printBagNum))])]),t._v(" "),i("b",[t._v("冲印袋")])]),t._v(" "),i("span",{staticClass:"submit",on:{click:t.goPrint}},[t._v("立即冲印")])])],1)},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement;return(t._self._c||e)("div",{class:t.slideClass},[t._t("default")],2)},staticRenderFns:[]}},,,function(t,e){}]),[57]);'
a = a.encode('utf-8')
b = b.encode('utf-8')
m.update(a)
print(m.hexdigest())
m.update(b)
print(m.hexdigest())
