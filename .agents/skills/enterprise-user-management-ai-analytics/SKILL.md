---
name: enterprise-user-management-ai-analytics
description: Full-stack enterprise user management system with AI-powered analytics for task tracking, ticket management, and predictive insights
triggers:
  - "help me set up the enterprise user management system"
  - "how do I integrate AI analytics into the user management app"
  - "show me how to create user roles and permissions"
  - "implement task tracking with AI burnout detection"
  - "configure the ML service for risk prediction"
  - "set up JWT authentication for the user system"
  - "create a ticket classification system with AI"
  - "build an admin dashboard with analytics"
---

# Enterprise User Management System with AI Analytics

> Skill by [ara.so](https://ara.so) — Data Skills collection.

## Overview

Enterprise User Management System with AI Analytics is a full-stack JavaScript/Node.js application that combines traditional user management with AI-powered insights. It provides user authentication, task tracking with Kanban boards, support ticket management, and ML-based analytics including risk detection, anomaly detection, burnout analysis, and predictive project insights.

**Key Components:**
- **Frontend**: React.js application for user and admin interfaces
- **Backend**: Node.js/Express REST API with JWT authentication
- **ML Service**: FastAPI-based AI service using scikit-learn and River
- **Database**: MongoDB for data persistence

## Installation

### Clone and Setup

```bash
# Clone repository
git clone https://github.com/Nareshkumar2583/Enterprise-User-Management-System-with-AI-Analytics.git
cd Enterprise-User-Management-System-with-AI-Analytics

# Install backend dependencies
cd backend
npm install

# Install frontend dependencies
cd ../frontend
npm install

# Install ML service dependencies
cd ../ml-service
pip install -r requirements.txt
```

### Environment Configuration

**Backend (.env)**
```bash
# backend/.env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/enterprise_user_mgmt
JWT_SECRET=your_jwt_secret_key_here
JWT_EXPIRE=7d
NODE_ENV=development
ML_SERVICE_URL=http://localhost:8000
```

**Frontend (.env)**
```bash
# frontend/.env
REACT_APP_API_URL=http://localhost:5000/api
REACT_APP_ML_SERVICE_URL=http://localhost:8000
```

**ML Service (.env)**
```bash
# ml-service/.env
DATABASE_URL=mongodb://localhost:27017/enterprise_user_mgmt
MODEL_PATH=./models
LOG_LEVEL=INFO
```

### Start Services

```bash
# Terminal 1: Start backend
cd backend
npm start

# Terminal 2: Start ML service
cd ml-service
uvicorn main:app --reload --port 8000

# Terminal 3: Start frontend
cd frontend
npm start
```

## Backend API Reference

### Authentication Endpoints

```javascript
// Register new user
POST /api/auth/register
Content-Type: application/json

{
  "username": "john.doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "role": "user"
}

// Login
POST /api/auth/login
{
  "email": "john@example.com",
  "password": "SecurePass123!"
}

// Response includes JWT token
{
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": { "id": "...", "email": "...", "role": "..." }
}
```

### User Management (Admin)

```javascript
// Get all users
GET /api/users
Authorization: Bearer <token>

// Update user
PUT /api/users/:userId
Authorization: Bearer <token>
{
  "role": "admin",
  "status": "active"
}

// Delete user
DELETE /api/users/:userId
Authorization: Bearer <token>
```

### Task Management

```javascript
// Create task
POST /api/tasks
Authorization: Bearer <token>
{
  "title": "Implement AI feature",
  "description": "Add burnout detection",
  "assignedTo": "userId",
  "priority": "high",
  "dueDate": "2026-05-01",
  "status": "todo"
}

// Update task status
PATCH /api/tasks/:taskId/status
{
  "status": "in-progress"
}

// Get user tasks
GET /api/tasks/user/:userId
Authorization: Bearer <token>
```

### Ticket Management

```javascript
// Create support ticket
POST /api/tickets
Authorization: Bearer <token>
{
  "title": "Login issue",
  "description": "Cannot access dashboard",
  "priority": "medium",
  "category": "technical"
}

// AI-powered ticket classification
POST /api/tickets/:ticketId/classify
Authorization: Bearer <token>

// Get tickets with filters
GET /api/tickets?status=open&priority=high
Authorization: Bearer <token>
```

## Frontend Integration Patterns

### Authentication Hook

```javascript
// src/hooks/useAuth.js
import { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const useAuth = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      fetchUser();
    } else {
      setLoading(false);
    }
  }, []);

  const fetchUser = async () => {
    try {
      const response = await axios.get(`${API_URL}/auth/me`);
      setUser(response.data);
    } catch (error) {
      localStorage.removeItem('token');
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    const response = await axios.post(`${API_URL}/auth/login`, {
      email,
      password
    });
    localStorage.setItem('token', response.data.token);
    axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;
    setUser(response.data.user);
    return response.data;
  };

  const logout = () => {
    localStorage.removeItem('token');
    delete axios.defaults.headers.common['Authorization'];
    setUser(null);
  };

  return { user, loading, login, logout };
};
```

### Task Kanban Board Component

```javascript
// src/components/TaskBoard.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

const TaskBoard = ({ userId }) => {
  const [tasks, setTasks] = useState({
    todo: [],
    inProgress: [],
    done: []
  });

  useEffect(() => {
    fetchTasks();
  }, [userId]);

  const fetchTasks = async () => {
    try {
      const response = await axios.get(`${API_URL}/tasks/user/${userId}`);
      const categorized = {
        todo: response.data.filter(t => t.status === 'todo'),
        inProgress: response.data.filter(t => t.status === 'in-progress'),
        done: response.data.filter(t => t.status === 'done')
      };
      setTasks(categorized);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  const updateTaskStatus = async (taskId, newStatus) => {
    try {
      await axios.patch(`${API_URL}/tasks/${taskId}/status`, {
        status: newStatus
      });
      fetchTasks();
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const TaskCard = ({ task }) => (
    <div className="task-card" draggable>
      <h4>{task.title}</h4>
      <p>{task.description}</p>
      <span className={`priority-${task.priority}`}>
        {task.priority}
      </span>
    </div>
  );

  return (
    <div className="kanban-board">
      <div className="column">
        <h3>To Do</h3>
        {tasks.todo.map(task => (
          <TaskCard key={task._id} task={task} />
        ))}
      </div>
      <div className="column">
        <h3>In Progress</h3>
        {tasks.inProgress.map(task => (
          <TaskCard key={task._id} task={task} />
        ))}
      </div>
      <div className="column">
        <h3>Done</h3>
        {tasks.done.map(task => (
          <TaskCard key={task._id} task={task} />
        ))}
      </div>
    </div>
  );
};

export default TaskBoard;
```

## ML Service API Integration

### Risk Prediction

```javascript
// Predict user risk level
const predictUserRisk = async (userId, userData) => {
  const ML_URL = process.env.REACT_APP_ML_SERVICE_URL;
  
  try {
    const response = await axios.post(`${ML_URL}/predict/risk`, {
      user_id: userId,
      task_completion_rate: userData.completionRate,
      avg_response_time: userData.avgResponseTime,
      failed_login_attempts: userData.failedLogins,
      inactive_days: userData.inactiveDays
    });
    
    return response.data;
    // { risk_level: "high", confidence: 0.87, factors: [...] }
  } catch (error) {
    console.error('Risk prediction error:', error);
    return null;
  }
};
```

### Burnout Detection

```javascript
// Detect employee burnout risk
const detectBurnout = async (userId) => {
  const ML_URL = process.env.REACT_APP_ML_SERVICE_URL;
  
  try {
    const response = await axios.post(`${ML_URL}/predict/burnout`, {
      user_id: userId
    });
    
    return response.data;
    // { 
    //   burnout_risk: "moderate",
    //   score: 0.65,
    //   recommendations: ["Reduce workload", "Schedule time off"]
    // }
  } catch (error) {
    console.error('Burnout detection error:', error);
    return null;
  }
};

// Usage in admin dashboard
const AdminDashboard = () => {
  const [burnoutAlerts, setBurnoutAlerts] = useState([]);

  useEffect(() => {
    checkBurnoutForAllUsers();
  }, []);

  const checkBurnoutForAllUsers = async () => {
    const users = await fetchAllUsers();
    const alerts = [];
    
    for (const user of users) {
      const burnoutData = await detectBurnout(user.id);
      if (burnoutData && burnoutData.burnout_risk !== 'low') {
        alerts.push({
          userId: user.id,
          userName: user.name,
          ...burnoutData
        });
      }
    }
    
    setBurnoutAlerts(alerts);
  };

  return (
    <div className="admin-dashboard">
      <h2>Burnout Alerts</h2>
      {burnoutAlerts.map(alert => (
        <div key={alert.userId} className="alert-card">
          <h3>{alert.userName}</h3>
          <span className={`risk-${alert.burnout_risk}`}>
            {alert.burnout_risk} risk
          </span>
          <ul>
            {alert.recommendations.map((rec, i) => (
              <li key={i}>{rec}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};
```

### Anomaly Detection

```javascript
// Detect anomalous behavior
const detectAnomaly = async (userId, activityData) => {
  const ML_URL = process.env.REACT_APP_ML_SERVICE_URL;
  
  try {
    const response = await axios.post(`${ML_URL}/detect/anomaly`, {
      user_id: userId,
      login_time: activityData.loginTime,
      location: activityData.location,
      device: activityData.device,
      actions: activityData.actions
    });
    
    if (response.data.is_anomaly) {
      // Trigger security alert
      await createSecurityAlert(userId, response.data);
    }
    
    return response.data;
  } catch (error) {
    console.error('Anomaly detection error:', error);
    return null;
  }
};
```

### Ticket Auto-Classification

```javascript
// Automatically classify and route tickets
const classifyTicket = async (ticketId, ticketContent) => {
  const ML_URL = process.env.REACT_APP_ML_SERVICE_URL;
  
  try {
    const response = await axios.post(`${ML_URL}/classify/ticket`, {
      ticket_id: ticketId,
      title: ticketContent.title,
      description: ticketContent.description
    });
    
    // Update ticket with AI classification
    await axios.patch(`${API_URL}/tickets/${ticketId}`, {
      category: response.data.category,
      priority: response.data.suggested_priority,
      assignedTo: response.data.suggested_assignee
    });
    
    return response.data;
  } catch (error) {
    console.error('Ticket classification error:', error);
    return null;
  }
};

// Auto-classify on ticket creation
const createTicketWithAI = async (ticketData) => {
  const ticket = await axios.post(`${API_URL}/tickets`, ticketData);
  const classification = await classifyTicket(ticket.data._id, ticketData);
  return { ...ticket.data, ...classification };
};
```

## Backend Implementation Patterns

### User Model with MongoDB

```javascript
// backend/models/User.js
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    unique: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  password: {
    type: String,
    required: true,
    minlength: 6
  },
  role: {
    type: String,
    enum: ['user', 'admin', 'manager'],
    default: 'user'
  },
  status: {
    type: String,
    enum: ['active', 'inactive', 'suspended'],
    default: 'active'
  },
  profile: {
    firstName: String,
    lastName: String,
    department: String,
    position: String
  },
  metrics: {
    tasksCompleted: { type: Number, default: 0 },
    avgResponseTime: { type: Number, default: 0 },
    lastLoginAt: Date,
    failedLoginAttempts: { type: Number, default: 0 }
  }
}, {
  timestamps: true
});

// Hash password before saving
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  this.password = await bcrypt.hash(this.password, 10);
  next();
});

// Method to compare passwords
userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model('User', userSchema);
```

### Task Model

```javascript
// backend/models/Task.js
const mongoose = require('mongoose');

const taskSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  description: String,
  status: {
    type: String,
    enum: ['todo', 'in-progress', 'done'],
    default: 'todo'
  },
  priority: {
    type: String,
    enum: ['low', 'medium', 'high', 'critical'],
    default: 'medium'
  },
  assignedTo: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  createdBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  dueDate: Date,
  completedAt: Date,
  timeTracked: {
    type: Number,
    default: 0
  },
  tags: [String]
}, {
  timestamps: true
});

module.exports = mongoose.model('Task', taskSchema);
```

### JWT Authentication Middleware

```javascript
// backend/middleware/auth.js
const jwt = require('jsonwebtoken');
const User = require('../models/User');

const auth = async (req, res, next) => {
  try {
    const token = req.header('Authorization')?.replace('Bearer ', '');
    
    if (!token) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findById(decoded.userId);

    if (!user || user.status !== 'active') {
      throw new Error('User not found or inactive');
    }

    req.user = user;
    req.token = token;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid authentication token' });
  }
};

// Role-based authorization
const authorize = (...roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ 
        error: 'Access denied: Insufficient permissions' 
      });
    }
    next();
  };
};

module.exports = { auth, authorize };
```

### Task Controller

```javascript
// backend/controllers/taskController.js
const Task = require('../models/Task');
const User = require('../models/User');
const axios = require('axios');

const ML_SERVICE_URL = process.env.ML_SERVICE_URL;

exports.createTask = async (req, res) => {
  try {
    const task = new Task({
      ...req.body,
      createdBy: req.user._id
    });
    await task.save();

    // Check for burnout risk when assigning new task
    if (req.body.assignedTo) {
      const burnoutCheck = await axios.post(
        `${ML_SERVICE_URL}/predict/burnout`,
        { user_id: req.body.assignedTo }
      ).catch(() => null);

      if (burnoutCheck?.data.burnout_risk === 'high') {
        // Send notification to admin
        console.warn(`High burnout risk for user ${req.body.assignedTo}`);
      }
    }

    res.status(201).json(task);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

exports.getUserTasks = async (req, res) => {
  try {
    const tasks = await Task.find({ 
      assignedTo: req.params.userId 
    })
    .populate('createdBy', 'username email')
    .sort({ createdAt: -1 });

    res.json(tasks);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.updateTaskStatus = async (req, res) => {
  try {
    const { status } = req.body;
    const task = await Task.findById(req.params.taskId);

    if (!task) {
      return res.status(404).json({ error: 'Task not found' });
    }

    task.status = status;
    if (status === 'done') {
      task.completedAt = new Date();
      
      // Update user metrics
      await User.findByIdAndUpdate(task.assignedTo, {
        $inc: { 'metrics.tasksCompleted': 1 }
      });
    }

    await task.save();
    res.json(task);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

exports.trackTime = async (req, res) => {
  try {
    const { timeInSeconds } = req.body;
    const task = await Task.findByIdAndUpdate(
      req.params.taskId,
      { $inc: { timeTracked: timeInSeconds } },
      { new: true }
    );

    res.json(task);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};
```

## ML Service Implementation (FastAPI)

### Main Application Structure

```python
# ml-service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import joblib
import numpy as np
from datetime import datetime
import os

app = FastAPI(title="Enterprise AI Analytics Service")

MODEL_PATH = os.getenv('MODEL_PATH', './models')

# Load pre-trained models
risk_model = joblib.load(f'{MODEL_PATH}/risk_model.pkl')
burnout_model = joblib.load(f'{MODEL_PATH}/burnout_model.pkl')
anomaly_model = joblib.load(f'{MODEL_PATH}/anomaly_model.pkl')

class RiskPredictionInput(BaseModel):
    user_id: str
    task_completion_rate: float
    avg_response_time: float
    failed_login_attempts: int
    inactive_days: int

class BurnoutPredictionInput(BaseModel):
    user_id: str
    weekly_hours: Optional[float] = 40.0
    tasks_assigned: Optional[int] = 0
    tasks_completed: Optional[int] = 0
    overtime_hours: Optional[float] = 0.0

class AnomalyDetectionInput(BaseModel):
    user_id: str
    login_time: str
    location: str
    device: str
    actions: List[str]

@app.post("/predict/risk")
async def predict_risk(data: RiskPredictionInput):
    try:
        features = np.array([[
            data.task_completion_rate,
            data.avg_response_time,
            data.failed_login_attempts,
            data.inactive_days
        ]])
        
        risk_score = risk_model.predict_proba(features)[0][1]
        risk_level = "high" if risk_score > 0.7 else "medium" if risk_score > 0.4 else "low"
        
        return {
            "user_id": data.user_id,
            "risk_level": risk_level,
            "risk_score": float(risk_score),
            "confidence": float(np.max(risk_model.predict_proba(features))),
            "factors": {
                "completion_rate": data.task_completion_rate,
                "response_time": data.avg_response_time,
                "failed_logins": data.failed_login_attempts
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/burnout")
async def predict_burnout(data: BurnoutPredictionInput):
    try:
        workload_ratio = data.tasks_assigned / max(data.tasks_completed, 1)
        features = np.array([[
            data.weekly_hours,
            data.tasks_assigned,
            data.tasks_completed,
            data.overtime_hours,
            workload_ratio
        ]])
        
        burnout_score = burnout_model.predict_proba(features)[0][1]
        risk = "high" if burnout_score > 0.7 else "moderate" if burnout_score > 0.4 else "low"
        
        recommendations = []
        if data.weekly_hours > 45:
            recommendations.append("Reduce weekly working hours")
        if data.overtime_hours > 10:
            recommendations.append("Limit overtime to prevent exhaustion")
        if workload_ratio > 1.5:
            recommendations.append("Redistribute workload - too many pending tasks")
        if not recommendations:
            recommendations.append("Maintain current work-life balance")
        
        return {
            "user_id": data.user_id,
            "burnout_risk": risk,
            "score": float(burnout_score),
            "recommendations": recommendations,
            "metrics": {
                "weekly_hours": data.weekly_hours,
                "workload_ratio": workload_ratio,
                "overtime_hours": data.overtime_hours
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detect/anomaly")
async def detect_anomaly(data: AnomalyDetectionInput):
    try:
        # Feature engineering for anomaly detection
        login_hour = int(data.login_time.split(':')[0])
        is_unusual_time = 1 if login_hour < 6 or login_hour > 22 else 0
        action_count = len(data.actions)
        
        features = np.array([[
            login_hour,
            is_unusual_time,
            action_count,
            hash(data.location) % 100,
            hash(data.device) % 100
        ]])
        
        is_anomaly = anomaly_model.predict(features)[0] == -1
        anomaly_score = anomaly_model.score_samples(features)[0]
        
        return {
            "user_id": data.user_id,
            "is_anomaly": bool(is_anomaly),
            "anomaly_score": float(anomaly_score),
            "severity": "high" if anomaly_score < -2 else "medium" if anomaly_score < -1 else "low",
            "factors": {
                "unusual_login_time": bool(is_unusual_time),
                "action_count": action_count,
                "location": data.location,
                "device": data.device
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/classify/ticket")
async def classify_ticket(ticket_data: dict):
    try:
        # Simple keyword-based classification (can be enhanced with NLP)
        title = ticket_data.get('title', '').lower()
        description = ticket_data.get('description', '').lower()
        text = f"{title} {description}"
        
        # Category classification
        if any(word in text for word in ['login', 'password', 'access', 'authentication']):
            category = 'authentication'
            priority = 'high'
        elif any(word in text for word in ['bug', 'error', 'crash', 'not working']):
            category = 'technical'
            priority = 'high'
        elif any(word in text for word in ['feature', 'request', 'enhancement', 'improvement']):
            category = 'feature_request'
            priority = 'medium'
        elif any(word in text for word in ['question', 'how to', 'help']):
            category = 'support'
            priority = 'low'
        else:
            category = 'general'
            priority = 'medium'
        
        return {
            "ticket_id": ticket_data.get('ticket_id'),
            "category": category,
            "suggested_priority": priority,
            "confidence": 0.85,
            "keywords": [word for word in ['login', 'bug', 'feature', 'help'] if word in text]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ML Analytics"}
```

## Common Usage Patterns

### Admin Dashboard with AI Insights

```javascript
// src/pages/AdminDashboard.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AdminDashboard = () => {
  const [analytics, setAnalytics] = useState({
    totalUsers: 0,
    activeUsers: 0,
    highRiskUsers: [],
    burnoutAlerts: [],
    anomalies: []
  });

  useEffect(() => {
    fetchAnalytics();
    const interval = setInterval(fetchAnalytics, 300000); // Refresh every 5 min
    return () => clearInterval(interval);
  }, []);

  const fetchAnalytics = async () => {
    try {
      const users = await axios.get(`${process.env.REACT_APP_API_URL}/users`);
      const ML_URL = process.env.REACT_APP_ML_SERVICE_URL;
      
      const highRisk = [];
      const burnout = [];
      
      for (const user of users.data) {
        // Risk prediction
        const riskData = await axios.post(`${ML_URL}/predict/risk`, {
          user_id: user._id,
          task_completion_rate: user.metrics.tasksCompleted / 100,
          avg_response_time: user.metrics.avgResponseTime,
          failed_login_attempts: user.metrics.failedLoginAttempts,
          inactive_days: calculateInactiveDays(user.metrics.lastLoginAt)
        });
        
        if (riskData.data.risk_level === 'high') {
          highRisk.push({ ...user, riskData: riskData.data });
        }
        
        // Burnout check
        const burnoutData = await axios.post(`${ML_URL}/predict/burnout`, {
          user_id: user._id,
          weekly_hours: 45,
          tasks_assigned: user.metrics.tasksAssigned || 0,
          tasks_completed: user.metrics.tasksCompleted || 0,
          overtime_hours: user.metrics.overtimeHours || 0
        });
        
        if (burnoutData.data.burnout_risk !== 'low') {
          burnout.push({ ...user, burnoutData: burnoutData.data });
        }
      }
      
      setAnalytics({
        totalUsers: users.data.length,
        activeUsers: users.data.filter(u => u.status === 'active').length,
        highRiskUsers: highRisk,
        burnoutAlerts: burnout,
        anomalies: []
      });
    } catch (error) {
      console.error('Error fetching analytics:', error);
    }
  };

  const calculateInactiveDays = (lastLogin) => {
    if (!lastLogin) return 999;
    const days = Math.floor((Date.now() - new Date(lastLogin)) / (1000 * 60 * 60 * 24));
    return days;
  };

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Users</h3>
          <p className="stat-value">{analytics.totalUsers}</p>
        </div>
        <div className="stat-card">
          <h3>Active Users</h3>
          <p className="stat-value"
