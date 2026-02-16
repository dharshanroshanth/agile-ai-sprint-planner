import React from 'react';

// Badge component for displaying priority
export const PriorityBadge = ({ priority }) => {
  const colorMap = {
    LOW: 'bg-green-100 text-green-800',
    MEDIUM: 'bg-yellow-100 text-yellow-800',
    HIGH: 'bg-orange-100 text-orange-800',
    CRITICAL: 'bg-red-100 text-red-800',
  };

  return (
    <span className={`px-3 py-1 rounded-full text-sm font-semibold ${colorMap[priority]}`}>
      {priority}
    </span>
  );
};

// Badge component for sprint status
export const StatusBadge = ({ status }) => {
  const statusMap = {
    'active': 'bg-blue-100 text-blue-800',
    'completed': 'bg-green-100 text-green-800',
    'planning': 'bg-purple-100 text-purple-800',
    'paused': 'bg-gray-100 text-gray-800',
  };

  return (
    <span className={`px-2 py-1 rounded text-xs font-semibold ${statusMap[status] || statusMap.paused}`}>
      {status?.charAt(0).toUpperCase() + status?.slice(1)}
    </span>
  );
};

// Badge component for risk level
export const RiskBadge = ({ level }) => {
  const colorMap = {
    'low': 'bg-green-100 text-green-800',
    'medium': 'bg-yellow-100 text-yellow-800',
    'high': 'bg-red-100 text-red-800',
  };

  return (
    <span className={`px-3 py-1 rounded-full text-sm font-semibold ${colorMap[level]}`}>
      {level?.toUpperCase()} Risk
    </span>
  );
};

// Loading spinner
export const LoadingSpinner = () => (
  <div className="flex justify-center items-center p-8">
    <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
  </div>
);

// Error alert
export const ErrorAlert = ({ message, onClose }) => (
  <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-4 flex justify-between items-center">
    <span className="text-red-800 font-semibold">{message}</span>
    {onClose && (
      <button
        onClick={onClose}
        className="text-red-500 hover:text-red-700 text-xl"
      >
        ×
      </button>
    )}
  </div>
);

// Success notification  
export const SuccessNotification = ({ message, onClose }) => (
  <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-4 flex justify-between items-center">
    <span className="text-green-800 font-semibold">{message}</span>
    {onClose && (
      <button
        onClick={onClose}
        className="text-green-500 hover:text-green-700 text-xl"
      >
        ×
      </button>
    )}
  </div>
);

// Workload indicator
export const WorkloadIndicator = ({ used, total, percentage }) => {
  const percent = percentage || (used / total * 100);
  const color = percent <= 85 ? 'bg-green-500' : percent <= 100 ? 'bg-yellow-500' : 'bg-red-500';

  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 bg-gray-200 rounded-full h-2">
        <div
          className={`${color} h-2 rounded-full transition-all`}
          style={{ width: `${Math.min(percent, 100)}%` }}
        ></div>
      </div>
      <span className="text-xs font-semibold text-gray-700 w-12 text-right">
        {Math.round(percent)}%
      </span>
    </div>
  );
};

// Stat card
export const StatCard = ({ title, value, icon: Icon, color = 'blue' }) => {
  const colorMap = {
    blue: 'bg-blue-50 text-blue-600',
    green: 'bg-green-50 text-green-600',
    orange: 'bg-orange-50 text-orange-600',
    red: 'bg-red-50 text-red-600',
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-gray-600 text-sm font-medium">{title}</p>
          <p className="text-3xl font-bold text-gray-900 mt-2">{value}</p>
        </div>
        {Icon && (
          <div className={`${colorMap[color]} p-3 rounded-lg`}>
            <Icon className="w-6 h-6" />
          </div>
        )}
      </div>
    </div>
  );
};

// Form input
export const FormInput = ({
  label,
  type = 'text',
  placeholder,
  value,
  onChange,
  error,
  required,
}) => (
  <div className="mb-4">
    <label className="block text-sm font-semibold text-gray-700 mb-2">
      {label} {required && <span className="text-red-500">*</span>}
    </label>
    <input
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
        error ? 'border-red-500' : 'border-gray-300'
      }`}
    />
    {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
  </div>
);

// Form textarea
export const FormTextarea = ({
  label,
  placeholder,
  value,
  onChange,
  rows = 4,
  error,
  required,
}) => (
  <div className="mb-4">
    <label className="block text-sm font-semibold text-gray-700 mb-2">
      {label} {required && <span className="text-red-500">*</span>}
    </label>
    <textarea
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      rows={rows}
      className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
        error ? 'border-red-500' : 'border-gray-300'
      }`}
    />
    {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
  </div>
);

// Form select
export const FormSelect = ({
  label,
  options,
  value,
  onChange,
  error,
  required,
}) => (
  <div className="mb-4">
    <label className="block text-sm font-semibold text-gray-700 mb-2">
      {label} {required && <span className="text-red-500">*</span>}
    </label>
    <select
      value={value}
      onChange={onChange}
      className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
        error ? 'border-red-500' : 'border-gray-300'
      }`}
    >
      <option value="">Select an option</option>
      {options.map((opt) => (
        <option key={opt.value} value={opt.value}>
          {opt.label}
        </option>
      ))}
    </select>
    {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
  </div>
);

// Multi-select for skills
export const SkillsInput = ({ label, value = [], onChange, error, required }) => {
  const commonSkills = [
    'Python',
    'JavaScript',
    'React',
    'FastAPI',
    'Node.js',
    'SQL',
    'TypeScript',
    'Docker',
    'AWS',
    'Git',
  ];

  const toggleSkill = (skill) => {
    const newValue = value.includes(skill)
      ? value.filter((s) => s !== skill)
      : [...value, skill];
    onChange(newValue);
  };

  return (
    <div className="mb-4">
      <label className="block text-sm font-semibold text-gray-700 mb-2">
        {label} {required && <span className="text-red-500">*</span>}
      </label>
      <div className="flex flex-wrap gap-2">
        {commonSkills.map((skill) => (
          <button
            key={skill}
            type="button"
            onClick={() => toggleSkill(skill)}
            className={`px-3 py-1 rounded-full text-sm font-semibold transition-colors ${
              value.includes(skill)
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
            }`}
          >
            {skill}
          </button>
        ))}
      </div>
      {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
    </div>
  );
};
