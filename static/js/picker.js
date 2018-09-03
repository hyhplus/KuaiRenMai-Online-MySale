function getSelectValue(e) {
	return e.options[e.selectedIndex].value
}

function toggleAddAreaButtonStatus(e) {
	addAreaButton.disabled = !getSelectValue(e)
}
var customLocal = {
	weekdays: {
		shorthand: ["周日", "周一", "周二", "周三", "周四", "周五", "周六"],
		longhand: ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
	},
	months: {
		shorthand: ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
		longhand: ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
	},
	rangeSeparator: " 至 ",
	weekAbbreviation: "周",
	scrollTitle: "滚动切换",
	toggleTitle: "点击切换 12/24 小时时制"
};
$(".pick-datetime").flatpickr({
	enableTime: !0,
	minDate: "today",
	locale: customLocal
}), $(".select-area").distpicker();
var selectProvince = document.querySelector("#select-province"),
	selectCity = document.querySelector("#select-city"),
	addAreaButton = document.querySelector("#add-area"),
	showArea = document.querySelector(".show-area"),
	addedArea = [];
selectProvince.addEventListener("change", function() {
	toggleAddAreaButtonStatus(selectCity)
}), selectCity.addEventListener("change", function() {
	toggleAddAreaButtonStatus(selectCity)
}), addAreaButton.addEventListener("click", function() {

	var e = getSelectValue(selectCity);
	if(-1 !== addedArea.indexOf(e)) return $(".alert").alert(), -1;
	if(-1 === addedArea.indexOf(e)) {
		var t = document.createElement("li");




var el = $('#chengqu').val(); 

if(el == ""){
	$('#chengqu').val(el +e);
}else{
	$('#chengqu').val(el + " " + e);
}




t.className = "selected-area", t.textContent = e, showArea.appendChild(t), addedArea.push(e)
	}
}), showArea.addEventListener("click", function(e) {
	var t = e.target;
	

var el = $('#chengqu').val(); 
el = el.replace(t.textContent,'');
$('#chengqu').val(el);
	
	t.classList.contains("selected-area") && (showArea.removeChild(t), addedArea.splice(addedArea.indexOf(t.textContent), 1))
});