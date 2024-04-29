package com.example.testproject

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.ActivityResult

import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MyClasses : AppCompatActivity() {
    var Classes = arrayListOf<String>()
    lateinit var MyAdapter: ClassesAdapter

    private val startForResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result: ActivityResult ->
        if (result.resultCode == Activity.RESULT_OK) {
            val intent = result.data
            val updatedArray = intent?.getStringArrayListExtra("updated_array")
            if (updatedArray != null) {
                Classes = updatedArray
                MyAdapter.ClassesInAdapter = Classes
                MyAdapter.notifyDataSetChanged()
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_my_classes)
        val ClassList: RecyclerView = findViewById(R.id.ClassList)
        val addClass: Button = findViewById(R.id.add_class)
        val myTestsLink: Button = findViewById(R.id.my_tests_button)
        ClassList.layoutManager = LinearLayoutManager(this)
        MyAdapter = ClassesAdapter(Classes, this)
        ClassList.adapter = MyAdapter

        addClass.setOnClickListener {
            val intent = Intent(this, AddClassActivity::class.java)
            intent.putStringArrayListExtra("current_array", Classes)
            startForResult.launch(intent)
        }

        myTestsLink.setOnClickListener {
            val intent = Intent(this, MyTestsActivity::class.java)
            intent.putStringArrayListExtra("current_array", Classes)
            startActivity(intent)
        }
    }
}