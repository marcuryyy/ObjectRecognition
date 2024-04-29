package com.example.testproject

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat


class AddClassActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_add_class)
        val className: EditText = findViewById(R.id.class_name)
        val add_button: Button = findViewById(R.id.button_create_class)
        val currentArray = intent.getStringArrayListExtra("current_array")?: arrayListOf()

        add_button.setOnClickListener {
            val class_label: String = className.text.toString()
            if(class_label != "") {
                val updatedArray = ArrayList(currentArray)
                updatedArray.add(class_label)
                val returnIntent = Intent()
                className.text.clear()
                returnIntent.putStringArrayListExtra("updated_array", updatedArray)
                setResult(Activity.RESULT_OK, returnIntent)
                finish()
            } else Toast.makeText(this, "Нет названия класса!", Toast.LENGTH_LONG).show()
        }
    }
}