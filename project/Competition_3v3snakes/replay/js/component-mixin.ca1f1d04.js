(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["component-mixin"],{"397a":function(t,e,a){"use strict";a("5943")},5943:function(t,e,a){},"69bf":function(t,e,a){"use strict";a("b3a6")},"6ef2":function(t,e,a){"use strict";a("9d84")},"9d84":function(t,e,a){},"9ee5":function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"mixin-components-container"},[a("el-row",[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Buttons")])]),a("div",{staticStyle:{"margin-bottom":"50px"}},[a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn blue-btn",attrs:{to:"/documentation/index"}},[t._v(" Documentation ")])],1),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn light-blue-btn",attrs:{to:"/icon/index"}},[t._v(" Icons ")])],1),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn pink-btn",attrs:{to:"/excel/export-excel"}},[t._v(" Excel ")])],1),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn green-btn",attrs:{to:"/table/complex-table"}},[t._v(" Table ")])],1),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn tiffany-btn",attrs:{to:"/example/create"}},[t._v(" Form ")])],1),a("el-col",{staticClass:"text-center",attrs:{span:4}},[a("router-link",{staticClass:"pan-btn yellow-btn",attrs:{to:"/theme/index"}},[t._v(" Theme ")])],1)],1)])],1),a("el-row",{staticStyle:{"margin-top":"50px"},attrs:{gutter:20}},[a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Material Design 的input")])]),a("div",{staticStyle:{height:"100px"}},[a("el-form",{attrs:{model:t.demo,rules:t.demoRules}},[a("el-form-item",{attrs:{prop:"title"}},[a("material-input",{attrs:{id:"material-input-demo",icon:"el-icon-search",name:"title",placeholder:"输入标题"},model:{value:t.demo.title,callback:function(e){t.$set(t.demo,"title",e)},expression:"demo.title"}},[t._v(" 标题 ")])],1)],1)],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("图片hover效果")])]),a("div",{staticClass:"component-item"},[a("pan-thumb",{attrs:{width:"100px",height:"100px",image:"https://wpimg.wallstcn.com/577965b9-bb9e-4e02-9f0c-095b41417191"}},[t._v(" vue-typescript-admin ")])],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("水波纹 waves v-directive")])]),a("div",{staticClass:"component-item"},[a("el-button",{directives:[{name:"waves",rawName:"v-waves"}],attrs:{type:"primary"}},[t._v(" 水波纹效果 ")])],1)])],1),a("el-col",{attrs:{span:6}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("hover text")])]),a("div",{staticClass:"component-item"},[a("mallki",{attrs:{"class-name":"mallki-text",text:"vue-typescript-admin"}})],1)])],1)],1),a("el-row",{staticStyle:{"margin-top":"50px"},attrs:{gutter:20}},[a("el-col",{attrs:{span:8}},[a("el-card",{staticClass:"box-card"},[a("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[a("span",[t._v("Share")])]),a("div",{staticClass:"component-item",staticStyle:{height:"420px"}},[a("dropdown-menu",{staticStyle:{margin:"0 auto"},attrs:{items:t.articleList,title:"系列文章"}})],1)])],1)],1)],1)},i=[],n=a("d4ec"),r=a("262e"),l=a("2caf"),c=a("9ab4"),o=a("1b40"),p=a("3cbc"),d=a("da80"),u=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a",{staticClass:"link--mallki",class:t.className,attrs:{href:"#"}},[t._v(" "+t._s(t.text)+" "),a("span",{attrs:{"data-letters":t.text}}),a("span",{attrs:{"data-letters":t.text}})])},b=[],m=function(t){Object(r["a"])(a,t);var e=Object(l["a"])(a);function a(){return Object(n["a"])(this,a),e.apply(this,arguments)}return a}(o["c"]);Object(c["a"])([Object(o["b"])({default:""})],m.prototype,"className",void 0),Object(c["a"])([Object(o["b"])({default:"vue-typescript-admin"})],m.prototype,"text",void 0),m=Object(c["a"])([Object(o["a"])({name:"Mallki"})],m);var v=m,h=v,f=(a("397a"),a("2877")),x=Object(f["a"])(h,u,b,!1,null,"6e1637c9",null),j=x.exports,C=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"share-dropdown-menu",class:{active:t.isActive}},[a("div",{staticClass:"share-dropdown-menu-wrapper"},[a("span",{staticClass:"share-dropdown-menu-title",on:{click:function(e){return e.target!==e.currentTarget?null:t.clickTitle(e)}}},[t._v(t._s(t.title))]),t._l(t.items,(function(e,s){return a("div",{key:s,staticClass:"share-dropdown-menu-item"},[e.href?a("a",{attrs:{href:e.href,target:"_blank"}},[t._v(t._s(e.title))]):a("span",[t._v(t._s(e.title))])])}))],2)])},_=[],O=a("bee2"),w=function(t){Object(r["a"])(a,t);var e=Object(l["a"])(a);function a(){var t;return Object(n["a"])(this,a),t=e.apply(this,arguments),t.isActive=!1,t}return Object(O["a"])(a,[{key:"clickTitle",value:function(){this.isActive=!this.isActive}}]),a}(o["c"]);Object(c["a"])([Object(o["b"])({default:function(){return[]}})],w.prototype,"items",void 0),Object(c["a"])([Object(o["b"])({default:"vue"})],w.prototype,"title",void 0),w=Object(c["a"])([Object(o["a"])({name:"DropdownMenu"})],w);var g=w,k=g,y=(a("69bf"),Object(f["a"])(k,C,_,!1,null,"b0daaa5c",null)),M=y.exports,S=function(t){Object(r["a"])(a,t);var e=Object(l["a"])(a);function a(){var t;return Object(n["a"])(this,a),t=e.apply(this,arguments),t.validateLength=function(t,e,a){6!==e.length?a(new Error("请输入六个字符")):a()},t.demo={title:""},t.demoRules={title:[{validator:t.validateLength,trigger:"change"}]},t.articleList=[{title:"基础篇",href:"https://juejin.im/post/59097cd7a22b9d0065fb61d2"},{title:"登录权限篇",href:"https://juejin.im/post/591aa14f570c35006961acac"},{title:"实战篇",href:"https://juejin.im/post/593121aa0ce4630057f70d35"},{title:"vue-admin-template 篇",href:"https://juejin.im/post/595b4d776fb9a06bbe7dba56"},{title:"v4.0 篇",href:"https://juejin.im/post/5c92ff94f265da6128275a85"},{title:"优雅的使用 icon",href:"https://juejin.im/post/59bb864b5188257e7a427c09"}],t}return a}(o["c"]);S=Object(c["a"])([Object(o["a"])({name:"ComponentMixinDemo",components:{DropdownMenu:M,MaterialInput:d["a"],Mallki:j,PanThumb:p["a"]}})],S);var T=S,D=T,E=(a("6ef2"),Object(f["a"])(D,s,i,!1,null,"63ed4de4",null));e["default"]=E.exports},b3a6:function(t,e,a){}}]);