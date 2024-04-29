package com.example.testproject

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MyTestsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_my_tests)
        val my_classes_link: Button = findViewById(R.id.my_classes_button)
        val add_test_button: Button = findViewById(R.id.add_test_button)
        val currentArray = intent.getStringArrayListExtra("current_array")?: arrayListOf()
        my_classes_link.setOnClickListener {
            val intent = Intent(this, MyClasses::class.java)
            val returnIntent = Intent()
            returnIntent.putStringArrayListExtra("updated_array", currentArray)
            setResult(Activity.RESULT_OK, returnIntent)
            finish()
        }
        //TODO add_test_button
    }
}