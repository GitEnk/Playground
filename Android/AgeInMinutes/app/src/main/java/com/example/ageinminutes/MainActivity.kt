package com.example.ageinminutes

import android.app.DatePickerDialog
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btnSelectDate = findViewById<Button>(R.id.btnSelectDate)

        btnSelectDate.setOnClickListener {view ->
            clickDatePicker(view)
            Toast.makeText(this,"Button works", Toast.LENGTH_LONG).show()
        }
    }

    fun clickDatePicker(view: View){
        val myCalendar = Calendar.getInstance()
        var year = myCalendar.get(Calendar.YEAR)
        val month = myCalendar.get(Calendar.MONTH)
        val day = myCalendar.get(Calendar.DAY_OF_MONTH)
        val dpd = DatePickerDialog(this, DatePickerDialog.OnDateSetListener {
                view, selectedYear, selectedMonth, selectedDayOfMonth ->
            Toast.makeText(this, "$selectedYear-${selectedMonth+1}-$selectedDayOfMonth", Toast.LENGTH_SHORT).show()
                val selectedDate = "$selectedYear-${selectedMonth+1}-$selectedDayOfMonth"
                val tvSelectedDate = findViewById<TextView>(R.id.tvSelectedDate)
                tvSelectedDate.setText(selectedDate)

                val sdf = SimpleDateFormat("yyyy-MM-dd", Locale.ENGLISH)
                val theDate = sdf.parse(selectedDate)
                val selectedDateInMinutes = theDate!!.time / 60000
                val currentDate = sdf.parse(sdf.format(System.currentTimeMillis()))
                val currentDateInMinutes = currentDate!!.time / 60000
                val diff = currentDateInMinutes - selectedDateInMinutes

                val tvAgeInMinutes = findViewById<TextView>(R.id.tvAgeInMin)
                tvAgeInMinutes.setText(diff.toString())
            },
            year,
            month,
            day)
            dpd.datePicker.setMaxDate(Date().time - 86400000)
            dpd.show()
    }
}