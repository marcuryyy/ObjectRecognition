package com.example.testproject

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class ClassDescription : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_class_description)
        val back_button: Button = findViewById(R.id.back_button)

        back_button.setOnClickListener {
            val intent = Intent(this, MyClasses::class.java)
            startActivity(intent)
        }
    }
}