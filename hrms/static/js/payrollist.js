{{ formset.management_form }}
function get_regular_amount(){
				{% for form in formset %}

					var rate= document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value
					var regular_days = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-regular_days").value
					var result = roundUp(rate * regular_days, 2) ;

					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-regular_amount").value = result;

					// check for ecola
					{% if base_payroll.company.get_company_rates.activate_ecola %}
						document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-ecola").value = {{base_payroll.company.get_company_rates.ecola_rate}} * regular_days;
					{% endif %}
					// alert({{ forloop.counter|add:'-1'}})
					// console.log({{ forloop.counter }})
					// calculate for net

					get_net()
				{% endfor %}
			}



			// function get_training_amount(){
			// 	var training_rate= document.getElementsByName("training_rate")[0].value
			// 	var training_days = document.getElementsByName("training_days")[0].value
			// 	var result = roundUp(training_rate*training_days * regular_days, 2) ;
			// 	document.getElementById("training_amount").value = result;
			//
			// 	// calculate for net
			// 	get_net()
			// }
			function get_sunday_amount(){
				{% for form in formset %}

					var rate= document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value
					var sunday = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday").value
					var result = roundUp(rate/8*1.3*sunday, 2) ;

					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_amount").value = result;

					// calculate for net

					get_net()
				{% endfor %}
			}

			function get_overtime_regular_amount(){
				{% for form in formset %}

					var rate= document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value
					var overtime_regular = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-overtime_regular").value
					var first_result = rate/8*1.25*overtime_regular;
					var result = roundUp(first_result, 2) ;

					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-overtime_regular_amount").value = result;
					// alert(first_result ,  result );
					console.log(first_result);
					console.log(result);
					get_net()
				{% endfor %}
			}

			function get_sunday_overtime_amount(){
				{% for form in formset %}

					var rate= document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value
					var sunday_overtime = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_overtime").value
					var first_result = rate/8*1.69*sunday_overtime;
					var result = roundUp(first_result, 2) ;

					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_overtime_amount").value = result;
					// alert(first_result ,  result );
					console.log(first_result);
					console.log(result);
					get_net()
				{% endfor %}
			}

			function get_sunday_nd_amount(){
				{% for form in formset %}

					var rate= document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value
					var sunday_nd = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_nd").value
					var first_result = rate/8*1.3*0.1*sunday_nd;
					var result = roundUp(first_result, 2) ;

					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_nd_amount").value = result;
					// alert(first_result ,  result );
					console.log(first_result);
					console.log(result);
					get_net()
				{% endfor %}
			}

			function get_rest_day_amount(){
				{% for form in formset %}
					var rest_days= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rest_days").value)
					var rate= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value)
					// var result = roundUp(rest_days*((rate/8*1.3*8−rate)+rate), 2) ;
					var result = roundUp(rest_days*((rate/8*1.3*8-rate)+rate), 2) ;
					alert(result)
					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rest_amount").value = result;

				{% endfor %}
				get_net()
			}

			function get_night_diff_amount(){
				{% for form in formset %}
					var night_diff= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-night_diff_days").value)
					var rate= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value)
					// var result = roundUp(rest_days*((rate/8*1.3*8−rate)+rate), 2) ;
					var result = roundUp(night_diff*(rate/8*0.1), 2) ;
					alert(result)
					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-night_diff_amount").value = result;

				{% endfor %}
				get_net()
			}

			function get_rest_day_overtime_amount(){
				{% for form in formset %}
					var rest_day_overtime= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rest_day_overtime").value)
					var rate= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value)
					var result = roundUp(rate/8*1.69*rest_day_overtime, 2) ;
					console.log(rate/8*1.69*rest_day_overtime);
					console.log(result);
					document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rest_day_overtime_amount").value = result;
				{% endfor %}
				get_net()
			}

			function get_special_holiday_amount(){
				{% for form in formset %}

					var rate= document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value
					var special_holiday_days = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-special_holiday_days").value
					var result = roundUp(rate*1.3*special_holiday_days, 2) ;
				  document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-special_holiday_amount").value = result;
				{% endfor %}
				// get_net()
			}

			function get_special_holiday_overtime_amount(){
				{% for form in formset %}
				var rate= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value)
				var special_holiday_overtime = Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-special_holiday_overtime").value)
				var result = roundUp(rate/8*1.69*special_holiday_overtime, 2) ;
				console.log(rate/8*1.69*special_holiday_overtime);
				console.log(result);
			  document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-special_holiday_overtime_amount").value = result;

				// get_net()
				{% endfor %}
			}

			function get_tardiness_undertime_regular_amount(){
				{% for form in formset %}
					var rate= Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rate").value)
					var tardiness_undertime_regular = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-tardiness_undertime_regular").value
					var result = roundUp(rate/8*tardiness_undertime_regular, 2) ;
					console.log(rate/8*tardiness_undertime_regular);
					console.log(result);
				  document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-tardiness_undertime_regular_amount").value = result;

					get_net()
				{% endfor %}
			}

			function get_uniform(){
				get_net()
			}
			function get_medical(){
				get_net()
			}
			function get_canteen(){
				get_net()
			}
			function get_gatepass(){
				get_net()
			}
			function get_vale(){
				get_net()
			}
			function get_pants(){
				get_net()
			}
			function get_service_fee(){
				get_net()
			}
			function get_thirteenth_month(){
				get_net()
			}
			function get_sil(){
				get_net()
			}
			function get_tshirt(){
				get_net()
			}
			function get_rf(){
				get_net()
			}

			function get_house(){
				get_net()
			}

			function get_misc(){
				get_net()
			}


			function get_net(){
				// calculate for net
				{% for form in formset %}

					var regular_days = document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-regular_days").value

					if (regular_days > 0) {
						var net = Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-regular_amount").value) +  Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-overtime_regular_amount").value)
						+ Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rest_amount").value) + Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rest_day_overtime_amount").value)
						+ Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-special_holiday_amount").value) + Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-special_holiday_overtime_amount").value) + Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-ecola").value)
						+ Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_amount").value)
						+ Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_overtime_amount").value)
						+ Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sunday_nd_amount").value)
						console.log(net);

						net = net - Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-tardiness_undertime_regular_amount").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-gatepass").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-uniform").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-medical").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-canteen").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sss").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-pagibig").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-philhealth").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-vale").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-pants").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-service_fee").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-thirteenth_month").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-sil").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-tshirt").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-rf").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-house").value)
											- Number(document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-misc").value)
						document.getElementById("id_form-{{ forloop.counter|add:'-1' }}-net_amount").value = net
					}

				{% endfor %}
			}


			function roundUp(num, precision) {
		    var numStr = num.toString();
		     var newNum = num.toFixed(precision);

		      // Handle for case: roundUp(2.555, 2) = 2.56
		      var rest = (num - newNum).toFixed(precision + 1);
		      var pw = Math.pow(10, precision);

		      if (rest * pw  >= 0.5) {
		        var roundUpStr = newNum + '9';
		        return (Number(roundUpStr)).toFixed(precision);
		      }

		      return Number(newNum);
	  	}